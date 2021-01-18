from enums.DistanceTypes import DistanceTypes
from enums.PreprocessTypesEnum import PreprocessType
from preprocessors.DataFramePreprocessor import DataFramePreprocessor


class PreprocessorFactory:
    def create(self, distance: str):
        if distance == DistanceTypes.EUCLIDEAN.value[0]:
            return DataFramePreprocessor(PreprocessType.NUMERIC_ONLY)
