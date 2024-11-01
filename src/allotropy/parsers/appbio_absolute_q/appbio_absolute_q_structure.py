from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from allotropy.allotrope.models.adm.pcr.benchling._2023._09.dpcr import ContainerType
from allotropy.allotrope.schema_mappers.adm.pcr.BENCHLING._2023._09.dpcr import (
    CalculatedDataItem,
    DataSource,
    Measurement,
    MeasurementGroup,
    Metadata,
)
from allotropy.exceptions import AllotropeConversionError
from allotropy.parsers.appbio_absolute_q.constants import (
    AGGREGATION_LOOKUP,
    BRAND_NAME,
    CALCULATED_DATA_REFERENCE,
    CalculatedDataSource,
    DEVICE_TYPE,
    PLATE_WELL_COUNT,
    PRODUCT_MANUFACTURER,
    SOFTWARE_NAME,
)
from allotropy.parsers.utils.pandas import map_rows, SeriesData
from allotropy.parsers.utils.uuids import random_uuid_str


@dataclass
class CalculatedItem:
    identifier: str
    name: str
    value: float
    unit: str
    source: CalculatedDataSource
    source_features: list[str]

    def get_data_sources(
        self, measurement_ids: list[str], calculated_data_ids: dict[str, str]
    ) -> list[DataSource]:
        if self.source == CalculatedDataSource.CALCULATED_DATA:
            return [
                DataSource(calculated_data_ids[source_feature], source_feature)
                for source_feature in self.source_features
            ]
        else:
            return [
                DataSource(identifier, self.source_features[0])
                for identifier in measurement_ids
            ]


@dataclass
class Group:
    well_identifier: str | None
    group_identifier: str
    target_identifier: str
    calculated_data: list[CalculatedItem]
    calculated_data_ids: dict[str, str]

    @property
    def name(self) -> str:
        return self.group_identifier.split("(")[0].strip()

    @property
    def key(self) -> str:
        return f"{self.name}_{self.target_identifier}"

    def get_calculated_data_ids(self) -> dict[str, str]:
        return {
            calculated_data.name: calculated_data.identifier
            for calculated_data in self.calculated_data
        }

    @staticmethod
    def create(data: SeriesData) -> Group:
        well_identifier = data.get(str, "Well")
        aggregation_type = AGGREGATION_LOOKUP[well_identifier]

        # TODO: if aggregation type is Replicate(Average), check for required columns
        # Raise if column(s) do not exist
        calculated_data_items = [
            CalculatedItem(
                random_uuid_str(),
                reference.name,
                data[float, reference.column],
                reference.unit,
                reference.source,
                reference.source_features,
            )
            for reference in CALCULATED_DATA_REFERENCE.get(aggregation_type, [])
        ]
        calculated_data_ids = {
            calculated_data.name: calculated_data.identifier
            for calculated_data in calculated_data_items
        }
        return Group(
            well_identifier=well_identifier,
            group_identifier=data[str, "Group"],
            target_identifier=data[str, "Target"],
            calculated_data=calculated_data_items,
            calculated_data_ids=calculated_data_ids,
        )

    @staticmethod
    def create_rows(data: pd.DataFrame) -> list[Group]:
        data = data.replace(np.nan, None)[data["Name"].isna()]
        return map_rows(data, Group.create)


@dataclass
class WellItem:
    name: str
    measurement_identifier: str
    well_identifier: str
    plate_identifier: str
    group_identifier: str
    target_identifier: str
    run_identifier: str
    instrument_identifier: str
    timestamp: str
    total_partition_count: float
    reporter_dye_setting: str
    concentration: float
    positive_partition_count: float

    @property
    def group_key(self) -> str:
        return f"{self.group_identifier}_{self.target_identifier}"

    @staticmethod
    def create(data: SeriesData) -> WellItem:
        return WellItem(
            name=data[str, "Name"],
            measurement_identifier=random_uuid_str(),
            well_identifier=data[str, "Well"],
            plate_identifier=data[str, "Plate"],
            group_identifier=data[str, "Group"],
            target_identifier=data[str, "Target"],
            run_identifier=data[str, "Run"],
            instrument_identifier=data[str, "Instrument"],
            timestamp=data[str, "Date"],
            total_partition_count=round(data[float, "Total"]),
            reporter_dye_setting=data[str, "Dye"],
            concentration=data[float, "Conc. cp/uL"],
            positive_partition_count=round(data[float, "Positives"]),
        )


@dataclass
class Well:
    items: list[WellItem]

    @staticmethod
    def create_wells(data: pd.DataFrame) -> list[Well]:
        if "Name" not in data:
            msg = "Input is missing required column 'Name'."
            raise AllotropeConversionError(msg)
        data = data.dropna(subset=["Name"]).replace(np.nan, None)
        return [
            Well(map_rows(well_data, WellItem.create))
            for _, well_data in data.groupby("Well")
        ]


def create_measurement_groups(wells: list[Well]) -> list[MeasurementGroup]:
    return [
        MeasurementGroup(
            experimental_data_identifier=well.items[0].run_identifier,
            plate_well_count=PLATE_WELL_COUNT,
            measurements=[
                Measurement(
                    identifier=item.measurement_identifier,
                    sample_identifier=item.name,
                    location_identifier=item.well_identifier,
                    measurement_time=item.timestamp,
                    plate_identifier=item.plate_identifier,
                    target_identifier=item.target_identifier,
                    total_partition_count=item.total_partition_count,
                    concentration=item.concentration,
                    positive_partition_count=item.positive_partition_count,
                    reporter_dye_setting=item.reporter_dye_setting,
                )
                for item in well.items
            ],
        )
        for well in wells
    ]


def create_calculated_data(
    wells: list[Well], groups: list[Group]
) -> list[CalculatedDataItem]:
    # Map measurement ids to group keys
    group_to_ids = defaultdict(list)
    for well in wells:
        for item in well.items:
            group_to_ids[item.group_key].append(item.measurement_identifier)

    return [
        CalculatedDataItem(
            identifier=calculated_data.identifier,
            name=calculated_data.name,
            value=calculated_data.value,
            unit=calculated_data.unit,
            data_sources=[
                DataSource(source.identifier, source.feature)
                for source in calculated_data.get_data_sources(
                    group_to_ids[group.key], group.calculated_data_ids
                )
            ],
        )
        for group in groups
        for calculated_data in group.calculated_data
    ]


def create_metadata(device_identifier: str, file_path: str) -> Metadata:
    return Metadata(
        device_identifier=device_identifier,
        brand_name=BRAND_NAME,
        device_type=DEVICE_TYPE,
        container_type=ContainerType.well_plate,
        software_name=SOFTWARE_NAME,
        product_manufacturer=PRODUCT_MANUFACTURER,
        file_name=Path(file_path).name,
        unc_path=file_path,
    )
