from flask import abort
from models.recommendMovies import RecommendMovies
from repositories.user.UserRepository import UserRepository

valid_distances = ['euclidean', 'cosine', 'manhattan']
valid_algs = ['Ward', 'maxLink', 'kmedoids', 'kmeans']


def validate_recommend_request(request: RecommendMovies):
    repo: UserRepository = UserRepository()
    if request.algorithm not in valid_algs:
        abort(400, 'Invalid algorithm')
    if request.distance not in valid_distances:
        abort(400, 'Invalid distance measure')
    if not repo.get_by_id(request.userId):
        abort(400, 'User with given id does not exists')
