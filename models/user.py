class User:
    id: str
    favourites: []
    recommended: []

    def __init__(self):
        pass

    def __init__(self, id, recommended, favourites):
        self.id = id
        self.favourites = favourites
        self.recommended = recommended

    @staticmethod
    def from_dict(dict):
        return User(dict['_id'], dict['recommended'], dict['favourites'])
