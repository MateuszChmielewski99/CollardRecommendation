from pandas import DataFrame


def map_dataframe_to_dict(dataframe: DataFrame, columns: list):
    result = []
    for index, row in dataframe.iterrows():
        result_dict: dict = {}
        for column in columns:
            result_dict[column] = row[column]
        result.append(result_dict)

    return result
