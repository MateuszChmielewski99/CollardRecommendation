from pandas import DataFrame


def get_rows_in(dataframe: DataFrame, column_name: str, value: list, asc: bool = False, sort: str = None):
    if column_name not in dataframe.columns.tolist():
        return None

    result: DataFrame = dataframe.loc[dataframe[column_name].isin(value)]

    if asc and not sort:
        raise Exception('Asc has no effect without sort')

    if sort:
        result = result.sort_values(by=sort, axis=0, ascending=asc)

    return result
