from pandas import DataFrame


def merge_dataframes(dataframes: list):
    result = DataFrame({})
    for _index, dataframe in enumerate(dataframes):
        result = result.append(dataframe)

    return result
