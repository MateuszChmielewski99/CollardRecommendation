from numpy import arange


def get_default_column_cluster(size: int):
    default = arange(size)
    default.fill('-1')
    return default
