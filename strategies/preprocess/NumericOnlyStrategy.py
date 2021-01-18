from .BasePreprocessStrategy import BasePreprcoessStrategy
from pandas import DataFrame
from numpy import number


class NumericOnlyStrategy(BasePreprcoessStrategy):
    def execute(self, dataframe: DataFrame):
        numeric = dataframe.select_dtypes(include=number)
        return numeric
