from enums.PreprocessTypesEnum import PreprocessType
from strategies.preprocess.NumericOnlyStrategy import NumericOnlyStrategy


class PreprocessStrategyFactory:
    def create(self, p_type: PreprocessType):
        if p_type == PreprocessType.NUMERIC_ONLY:
            return NumericOnlyStrategy()
