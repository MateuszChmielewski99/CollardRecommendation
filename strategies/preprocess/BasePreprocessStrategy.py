from pandas import DataFrame


class BasePreprcoessStrategy:
    def execute(self, dataframe: DataFrame):
        pass
