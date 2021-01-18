import unittest
from utils.get_rows_by import get_rows_by
from pandas import DataFrame
import numpy.testing as nt


class GetRowsByTest(unittest.TestCase):
    def test_should_return_value(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102]}
        dataframe = DataFrame(data=data)

        # when
        result = get_rows_by(dataframe, 'Id', 1)

        # then
        expected_data = {'Id': [1], 'B': [100]}
        expected_value = DataFrame(data=expected_data)
        nt.assert_array_equal(expected_value.values, result.values)

    def test_should_raise_on_invalid_column_name(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102]}
        dataframe = DataFrame(data=data)

        # when then
        with self.assertRaises(Exception):
            get_rows_by(dataframe, 'X')

    def test_should_raise_on_asc_without_sort(self):
        # given
        data = {'Id': [1, 2, 3], 'B': [100, 101, 102]}
        dataframe = DataFrame(data=data)

        # when then
        with self.assertRaises(Exception):
            get_rows_by(dataframe, 'Id', asc=True)

    def test_should_return_sorted_values(self):
        data = {'A': [3, 2, 1], 'B': [100, 101, 100]}
        dataframe = DataFrame(data=data)

        # when
        result = get_rows_by(dataframe=dataframe, column_name='B', value=100, sort='A', asc=True)

        # then
        expected_data = {'A': [1, 3], 'B': [100, 100]}
        expected_value = DataFrame(data=expected_data)
        nt.assert_array_equal(expected_value.values, result.values)
