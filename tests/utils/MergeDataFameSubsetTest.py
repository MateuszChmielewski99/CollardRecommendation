import unittest
from utils.merge_dataframes import merge_dataframes
from pandas import DataFrame
import numpy.testing as nt


class MergeDataFramesTest(unittest.TestCase):
    def test_should_merge_dataframes(self):
        # given
        data1 = {'Id': [1, 2, 3], 'B': ['a', 'b', 'c']}
        data2 = {'Id': [4, 5, 6], 'B': ['a', 'b', 'c']}
        data_frames = [DataFrame(data=data1), DataFrame(data=data2)]

        # when
        result = merge_dataframes(data_frames)

        # then
        expected_data = {'Id': [1, 2, 3, 4, 5, 6], 'B': ['a', 'b', 'c', 'a', 'b', 'c']}
        expected = DataFrame(data=expected_data)
        nt.assert_array_equal(expected.values, result.values)
