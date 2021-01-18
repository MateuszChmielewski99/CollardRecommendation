from settings import MONGO
from pymongo import MongoClient
from models.user import User


class UserRepository:
    mongo = MongoClient(MONGO)
    db = mongo.CollardMovie
    collection = db.users

    def get_by_id(self, id: str):
        return self.collection.find_one({'_id': id})

    def update(self, user: User):
        query = {'_id': user.id}
        update_query = {"$set": {"favourites": user.favourites, "recommended": user.recommended}}
        self.collection.update_one(query, update_query)
