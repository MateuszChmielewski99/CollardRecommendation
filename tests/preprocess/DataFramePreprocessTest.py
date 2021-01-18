import unittest
from sklearn.preprocessing import StandardScaler
from preprocessors.DataFramePreprocessor import DataFramePreprocessor
from enums.PreprocessTypesEnum import PreprocessType
from pandas import DataFrame
import numpy.testing as nt


class DataFramePreprocessTest(unittest.TestCase):
    def test_should_normalize_data_for_not_empty_list(self):
        # given
        preprocessor = DataFramePreprocessor(PreprocessType.NUMERIC_ONLY)
        data = {'A': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        dataframe = DataFrame(data=data)

        # when
        dataframe = preprocessor.preprocess(dataframe=dataframe, normalize=['A', 'B'])

        # then
        rdata = {'A': [1, 2, 3], 'B': [100, 101, 102]}
        result = DataFrame(data=rdata)
        result[['A', 'B']] = StandardScaler().fit_transform(dataframe[['A', 'B']])
        nt.assert_allclose(result.values, dataframe.values)

    def test_should_return_only_numeric_columns(self):
        # given
        preprocessor = DataFramePreprocessor(PreprocessType.NUMERIC_ONLY)
        data = {'A': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        dataframe = DataFrame(data=data)

        # when
        dataframe = preprocessor.preprocess(dataframe=dataframe)

        # then
        rdata = {'A': [1, 2, 3], 'B': [100, 101, 102]}
        result = DataFrame(data=rdata)
        nt.assert_allclose(result.values, dataframe.values)
