class RecommendMovies:
    userId: str
    algorithm: str
    distance: str
    divideByFirst: bool
    divideBySecond: bool
    divideByThird: bool
    groupNumber: int
    normalizeData: bool

    def __init__(self):
        pass

    def __init__(self, user_id, alghorithm, distance, first, second, third, groups, normalize):
        self.userId = user_id
        self.algorithm = alghorithm
        self.distance = distance
        self.divideByFirst = first
        self.divideBySecond = second
        self.divideByThird = third
        self.groupNumber = groups
        self.normalizeData = normalize

    @staticmethod
    def from_dict(dict):
        return RecommendMovies(dict['userId'], dict['algorithm'], dict['distance'], dict['divideByFirst'],
                               dict['divideBySecond'],
                               dict['divideByThird'], dict['groupNumber'], normalize=dict['normalizeData'])
