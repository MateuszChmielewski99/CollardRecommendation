from models.recommendMovies import RecommendMovies
from factories.DataFrameFactory import DataFrameFactory
from factories.ModelFactory import ModelFactory
from recommendator.Recommendator import Recommendator
from repositories.user.UserRepository import UserRepository
from models.user import User
from factories.PreprocessorFactory import PreprocessorFactory
from utils.map_to_dto import map_to_dto


class RecommendHandler:
    data_frame_factory = DataFrameFactory()
    model_factory = ModelFactory()
    preprocessor_factory = PreprocessorFactory()

    def handle(self, request: RecommendMovies):
        data_preprocessor = self.preprocessor_factory.create(request.distance)

        repository = UserRepository()

        recommendator = Recommendator(self.data_frame_factory, self.model_factory, data_preprocessor)

        user: User = User.from_dict(repository.get_by_id(request.userId))

        favourites_ids = list(map(lambda x: int(x['id']), user.favourites))

        recommended_movies = recommendator.get_recommended_movies(request, favourites_ids)

        dtos = list(map(lambda x: map_to_dto(x), recommended_movies))

        user.recommended = dtos
        repository.update(user)
