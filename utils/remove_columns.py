from pandas import DataFrame


def remove_columns(df: DataFrame, columns: list):
    df.drop(labels=columns, inplace=True, axis=1)
