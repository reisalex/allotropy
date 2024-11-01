from allotropy.allotrope.models.adm.pcr.benchling._2023._09.qpcr import ExperimentType
from allotropy.parsers.appbio_quantstudio_designandanalysis.appbio_quantstudio_designandanalysis_reader import (
    DesignQuantstudioReader,
)
from allotropy.parsers.appbio_quantstudio_designandanalysis.structure.generic.creator import (
    Creator,
)
from allotropy.parsers.appbio_quantstudio_designandanalysis.structure.generic.structure import (
    Data,
    Header,
)
from allotropy.parsers.appbio_quantstudio_designandanalysis.structure.primary_analysis.structure import (
    PrimaryAnalysisWellList,
)


class PrimaryAnalysisCreator(Creator):
    @classmethod
    def check_type(cls, reader: DesignQuantstudioReader) -> bool:
        return list(reader.data.keys()) == ["Results"]

    @classmethod
    def create(cls, reader: DesignQuantstudioReader) -> Data:
        header = Header.create(reader.header)
        wells = PrimaryAnalysisWellList.create(reader, header)
        return Data(
            header,
            wells,
            experiment_type=ExperimentType.presence_absence_qPCR_experiment,
            calculated_documents=[],
            reference_target=None,
            reference_sample=None,
        )
