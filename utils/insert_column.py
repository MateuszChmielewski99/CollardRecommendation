from pandas import DataFrame


def insert_column(dataframe: DataFrame, column_name: str, values: list, loc: int):
    dataframe.insert(column=column_name, value=values, allow_duplicates=True, loc=loc)
