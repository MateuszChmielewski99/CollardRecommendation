from enum import Enum


class DistanceTypes(Enum):
    EUCLIDEAN = 'euclidean',
    COSINE = 'cosine',
    CITY = 'manhattan'
