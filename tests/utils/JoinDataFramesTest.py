import unittest
from utils.join_dataframes_on import join_dataframes_on
from pandas import DataFrame
import numpy.testing as nt


class JoinDataFramesTest(unittest.TestCase):
    def test_should_merge_dataframes(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        dataframe = DataFrame(data=data)
        data2 = {'Id': [1, 2, 3], 'D': ['all', 'works', 'fine']}
        dataframe2 = DataFrame(data=data2)

        # when
        result = join_dataframes_on(dataframe, dataframe2, on='Id')

        # then
        expected_data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c'], 'D': ['all', 'works', 'fine']}
        expected = DataFrame(data=expected_data)
        nt.assert_array_equal(expected.values, result.values)

    def test_should_not_override_column(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        dataframe = DataFrame(data=data)
        data2 = {'Id': [1, 2, 3], 'B': [102, 101, 105], 'D': ['all', 'works', 'fine']}
        dataframe2 = DataFrame(data=data2)

        # when
        result = join_dataframes_on(dataframe, dataframe2, on='Id')

        # then
        expected_data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c'], 'D': ['all', 'works', 'fine']}
        expected = DataFrame(data=expected_data)
        nt.assert_array_equal(expected.values, result.values)

    def test_should_throw_error_on_invalid_value(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        dataframe = DataFrame(data=data)
        data2 = {'Id': [1, 2, 3], 'B': [102, 101, 105], 'D': ['all', 'works', 'fine']}
        dataframe2 = DataFrame(data=data2)

        # when
        with self.assertRaises(Exception):
            join_dataframes_on(dataframe, dataframe2, 'X')
