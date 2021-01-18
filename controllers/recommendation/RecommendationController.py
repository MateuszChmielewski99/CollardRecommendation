from flask_restful import Resource
from .parsers.custom_recommendation_parser import recommend_args
from handlers.RecommendHandler import RecommendHandler
from models.recommendMovies import RecommendMovies
from .validators.recommend_validator import validate_recommend_request


class RecommendationController(Resource):
    handler = RecommendHandler()

    def post(self):
        body = recommend_args.parse_args()
        request = RecommendMovies.from_dict(body)
        validate_recommend_request(request)
        self.handler.handle(request)
        return {'Ok': 'Ok'}
