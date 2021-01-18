from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn_extra.cluster import KMedoids


# valid_algs = ['Ward', 'maxLink', 'kmedoids', '']
class ModelFactory:
    def create_model(self, modelName: str, distance: str, groupNumber: int):
        return {
            'kmeans': KMeans(n_clusters=groupNumber),
            'Ward': AgglomerativeClustering(n_clusters=groupNumber, linkage='ward'),
            'maxLink': AgglomerativeClustering(n_clusters=groupNumber, linkage='complete', affinity=distance),
            'kmedoids': KMedoids(n_clusters=groupNumber, metric=distance)
        }.get(modelName, None)
