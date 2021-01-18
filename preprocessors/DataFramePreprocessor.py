from pandas import DataFrame
from strategies.preprocess import BasePreprocessStrategy
from factories.PreprocessStrategyFactory import PreprocessStrategyFactory
from enums.PreprocessTypesEnum import PreprocessType
from sklearn.preprocessing import StandardScaler


class DataFramePreprocessor:
    _strategy: BasePreprocessStrategy

    def __init__(self, p_type: PreprocessType):
        factory = PreprocessStrategyFactory()
        self._strategy = factory.create(p_type)

    def preprocess(self, dataframe: DataFrame, normalize: list = []):
        if len(normalize):
            dataframe[normalize] = StandardScaler().fit_transform(dataframe[normalize])

        return self._strategy.execute(dataframe)
