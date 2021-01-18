import unittest
from utils.insert_column import insert_column
from pandas import DataFrame
import numpy.testing as nt


class InsertColumnToDataFramesTest(unittest.TestCase):
    def test_should_insert_new_column(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102]}
        dataframe = DataFrame(data=data)

        # when
        insert_column(dataframe, 'C', values=['a', 'b', 'c'], loc=2)

        # then
        expected_data = {'Id': [1, 2, 3], 'B': [100, 101, 102], 'C': ['a', 'b', 'c']}
        expected = DataFrame(data=expected_data)
        nt.assert_array_equal(expected.values, dataframe.values)
