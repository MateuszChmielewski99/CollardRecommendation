from models.recommendMovies import RecommendMovies
from columns import numeric_columns
from utils.remove_columns import remove_columns
from utils.get_updated_cluster import get_updated_clusters
from utils.get_default_colum_cluster import get_default_column_cluster
from utils.merge_dataframes import merge_dataframes
from utils.join_dataframes_on import join_dataframes_on
from utils.insert_column import insert_column
from dataframe import df


class Clusterer:

    def __init__(self, data_factory, model_factory, data_preprocessor):
        self.data_frames_factory = data_factory
        self.model_factory = model_factory
        self.data_preprocessor = data_preprocessor

    def get_clustered_data_frame(self, request: RecommendMovies):
        datasets = self.data_frames_factory.create_data_frames_array(request.divideByFirst, request.divideBySecond,
                                                                     request.divideByThird)
        for index, subset in enumerate(datasets):
            if subset.shape[0] > 10:
                ids = subset['Id']
                remove_columns(subset, ['Id'])

                if request.normalizeData:
                    columns_to_normalize = numeric_columns
                else:
                    columns_to_normalize = []

                subset = self.data_preprocessor.preprocess(dataframe=subset, normalize=columns_to_normalize)
                model = self.model_factory.create_model(request.algorithm, request.distance, request.groupNumber)
                model.fit_predict(subset)
                labels = get_updated_clusters(model.labels_, index)
                insert_column(subset, column_name='Cluster', values=labels, loc=1)
                insert_column(subset, column_name='Id', values=ids, loc=0)

            else:
                default_labels = get_default_column_cluster(subset.shape[0])
                insert_column(subset, column_name='Cluster', values=default_labels, loc=1)
            datasets[index] = subset

        merged = merge_dataframes(datasets)
        result = join_dataframes_on(df, merged, on='Id')
        return result
