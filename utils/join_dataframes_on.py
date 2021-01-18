from pandas import DataFrame, merge


def join_dataframes_on(first: DataFrame, second: DataFrame, on: str):
    first_columns = first.columns.tolist()
    second_coulmns = second.columns.to_list()

    if on not in first_columns or on not in second_coulmns:
        raise Exception('Invalid on value')

    common_columns = set.intersection(set(first_columns), set(second_coulmns))
    common_columns.remove(on)
    second.drop(labels=common_columns, axis=1, inplace=True)

    return merge(first, second, on=on, how='left')
