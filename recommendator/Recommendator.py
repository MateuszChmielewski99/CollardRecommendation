from utils.get_rows_in import get_rows_in
from pandas import DataFrame, unique
from numpy import ndarray
from utils.get_rows_by import get_rows_by
from columns import movie_reference_columns
from utils.map_dataframe_to_dict import map_dataframe_to_dict
from clusterer.Clusterer import Clusterer
from models.recommendMovies import RecommendMovies


class Recommendator:

    def __init__(self, data_factory, model_factory, data_preprocessor):
        self.clusterer = Clusterer(data_factory=data_factory, model_factory=model_factory,
                                   data_preprocessor=data_preprocessor)

    def get_recommended_movies(self, request: RecommendMovies, favourite_movies_ids: list):
        dataframe = self.clusterer.get_clustered_data_frame(request)

        favourite_movies_df: DataFrame = get_rows_in(dataframe, column_name='Id', value=favourite_movies_ids)
        clusters: ndarray = unique(favourite_movies_df['Cluster'])

        movies = []

        for cluster in clusters:
            recommended = get_rows_by(dataframe=dataframe, value=cluster, column_name='Cluster', sort='IMDBScore')
            recommended.drop_duplicates(inplace=True, subset=['Title'])
            top_three = recommended[:3]
            movies.append(top_three)

        movies = list(map(lambda x: map_dataframe_to_dict(x, movie_reference_columns), movies))
        flat_list = [item for sublist in movies for item in sublist]

        return flat_list
