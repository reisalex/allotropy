# generated by datamodel-codegen:
#   filename:  electrophoresis.schema.json
#   timestamp: 2024-10-01T19:58:12+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueMilliAbsorbanceUnit,
    TQuantityValueMilliAbsorbanceUnitTimesMilliliter,
    TQuantityValueMilliAbsorbanceUnitTimesSecond,
    TQuantityValueMilliliter,
    TQuantityValueNanometer,
    TQuantityValueNumber,
    TQuantityValuePercent,
    TQuantityValueRelativeFluorescenceUnit,
    TQuantityValueRelativeFluorescenceUnitTimesMilliliter,
    TQuantityValueRelativeFluorescenceUnitTimesSecond,
    TQuantityValueSecondTime,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TBooleanValue,
    TClass,
    TDatacube,
    TDateTimeStampValue,
    TDateTimeValue,
    TDoubleValue,
    TIntegerValue,
    TQuantityValue,
    TStringValue,
    TUnit,
)


@dataclass(kw_only=True)
class AdmCoreREC202406ManifestSchema:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass(kw_only=True)
class OrderedItem:
    field_index: int | None = None


@dataclass(kw_only=True)
class CustomInformationDocumentItem:
    scalar_double_datum: TDoubleValue | None = None
    unit: TUnit | None = None
    scalar_string_datum: TStringValue | None = None
    scalar_timestamp_datum: TDateTimeValue | None = None
    scalar_boolean_datum: TBooleanValue | None = None
    datum_label: TStringValue | None = None


@dataclass(kw_only=True)
class CustomInformationAggregateDocument:
    custom_information_document: list[CustomInformationDocumentItem]


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class ElectronicProjectRecord:
    written_name: TStringValue
    description: Any | None = None
    start_time: TDateTimeValue | None = None


@dataclass(kw_only=True)
class ElectronicSignatureDocumentItem:
    account_identifier: TStringValue
    personal_name: TStringValue
    signature_role_type: TStringValue
    time: TStringValue
    identifier: TStringValue | None = None
    measurement_identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class ElectronicSignatureAggregateDocument:
    electronic_signature_document: list[ElectronicSignatureDocumentItem] | None = None


@dataclass(kw_only=True)
class ErrorDocumentItem:
    error: TStringValue
    error_feature: TStringValue | None = None


@dataclass(kw_only=True)
class ErrorAggregateDocument:
    error_document: list[ErrorDocumentItem] | None = None


@dataclass(kw_only=True)
class ImageDocumentItem:
    experimental_data_identifier: TStringValue | None = None
    index: TIntegerValue | None = None


@dataclass(kw_only=True)
class ImageAggregateDocument:
    image_document: list[ImageDocumentItem] | None = None


@dataclass(kw_only=True)
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    electronic_project_record: ElectronicProjectRecord | None = None


@dataclass(kw_only=True)
class StatisticsDocumentItem:
    statistical_feature: TClass


@dataclass(kw_only=True)
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass(kw_only=True)
class AnalysisSequenceDocument:
    written_name: TStringValue
    end_time: TDateTimeValue | None = None
    file_name: TStringValue | None = None
    identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    method_name: TStringValue | None = None
    start_time: TDateTimeValue | None = None
    UNC_path: TStringValue | None = None
    version_number: TStringValue | None = None


@dataclass(kw_only=True)
class DataSystemDocument:
    ASM_file_identifier: TStringValue
    data_system_instance_identifier: TStringValue
    file_name: TStringValue | None = None
    UNC_path: TStringValue | None = None
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None
    database_primary_key: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue | None = None
    brand_name: TStringValue | None = None
    description: Any | None = None
    device_document: list[DeviceDocumentItem] | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    detection_type: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None
    detector_wavelength_setting: TQuantityValueNanometer | None = None
    detector_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = (
        None
    )
    total_measurement_time_setting: TQuantityValueSecondTime | None = None
    read_interval_setting: TQuantityValueSecondTime | None = None
    number_of_scans_setting: TQuantityValueNumber | None = None
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = (
        None
    )
    excitation_wavelength_setting: TQuantityValueNanometer | None = None
    excitation_bandwidth_setting: TQuantityValueNanometer | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class Peak:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    peak_end: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    identifier: TStringValue | None = None
    relative_peak_height: TQuantityValuePercent | None = None
    written_name: TStringValue | None = None
    peak_height: TQuantityValue | None = None
    capacity_factor__chromatography_: TQuantityValueUnitless | None = None
    peak_area: TQuantityValue | None = None
    relative_peak_area: TQuantityValuePercent | None = None
    retention_time: TQuantityValueSecondTime | None = None
    retention_volume: TQuantityValueMilliliter | None = None
    peak_start: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    peak_selectivity__chromatography_: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution: TQuantityValueUnitless | None = None
    field_index: int | None = None
    chromatographic_peak_resolution_using_baseline_peak_widths: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height__JP14_: TQuantityValueUnitless | None = (
        None
    )
    peak_width_at_4_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_13_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_32_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_60_7___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_half_height: TQuantityValueSecondTime | None = None
    peak_width_at_5___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_baseline: TQuantityValueSecondTime | None = None
    peak_width_at_inflection: TQuantityValueSecondTime | None = None
    peak_width_at_10___of_height: TQuantityValueSecondTime | None = None
    peak_width: TQuantityValueSecondTime | None = None
    statistical_skew__chromatography_: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_5___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_10___height: TQuantityValueUnitless | None = None
    asymmetry_factor_squared_measured_at_10___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_squared_measured_at_4_4___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_measured_at_4_4___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_baseline: TQuantityValueUnitless | None = None
    chromatographic_peak_asymmetry_factor: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_statistical_moments: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates__chromatography_: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_60_7___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_32_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_13_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_4_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_tangent_method: TQuantityValueUnitless | None = None


@dataclass(kw_only=True)
class PeakList:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    peak: list[PeakItem] | list[Peak] | None = None


@dataclass(kw_only=True)
class DataRegionDocumentItem:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_region_end: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    data_region_identifier: TStringValue | None = None
    data_region_name: TStringValue | None = None
    data_region_area: TQuantityValue | None = None
    relative_data_region_area: TQuantityValuePercent | None = None
    data_region_start: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DataRegionAggregateDocument:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_region_document: list[DataRegionDocumentItem] | None = None


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    batch_identifier: TStringValue | None = None
    description: Any | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class PeakItem(OrderedItem):
    peak_height: TQuantityValueMilliAbsorbanceUnit | TQuantityValueRelativeFluorescenceUnit | None = (
        None
    )
    peak_area: TQuantityValueMilliAbsorbanceUnitTimesMilliliter | TQuantityValueMilliAbsorbanceUnitTimesSecond | TQuantityValueRelativeFluorescenceUnitTimesMilliliter | TQuantityValueRelativeFluorescenceUnitTimesSecond | None = (
        None
    )


@dataclass(kw_only=True)
class ProcessedDataDocument:
    peak_list: PeakList | None = None
    derived_electropherogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class ProcessedDataDocumentItem:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_processing_document: dict[str, Any] | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None
    peak_list: PeakList | None = None
    data_region_aggregate_document: DataRegionAggregateDocument | None = None
    derived_electropherogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class MeasurementDocument:
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    electropherogram_data_cube: TDatacube | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    detection_type: TStringValue | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    measurement_identifier: TStringValue | None = None
    measurement_time: TDateTimeStampValue | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    processed_data_document: ProcessedDataDocument | None = None
    absorption_profile_data_cube: TDatacube | None = None
    chromatogram_data_cube: TDatacube | None = None
    three_dimensional_ultraviolet_spectrum_data_cube: TDatacube | None = None
    fluorescence_emission_profile_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocument]
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class ElectrophoresisDocumentItem:
    analyst: TStringValue
    measurement_aggregate_document: MeasurementAggregateDocument
    electronic_project_record: ElectronicProjectRecord | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class ElectrophoresisAggregateDocument:
    electrophoresis_document: list[ElectrophoresisDocumentItem]
    analysis_sequence_document: AnalysisSequenceDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_system_document: DataSystemDocument | None = None
    device_system_document: DeviceSystemDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    electronic_signature_aggregate_document: ElectronicSignatureAggregateDocument | None = (
        None
    )
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    field_asm_manifest: AdmCoreREC202406ManifestSchema | str
    electrophoresis_aggregate_document: ElectrophoresisAggregateDocument | None = None
