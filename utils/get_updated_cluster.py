def get_updated_clusters(labels, index):
    updated_labels = []
    for label in labels:
        updated_labels.append(set_cluster_subgroup(index, label))
    return updated_labels


def set_cluster_subgroup(index, cluster_number):
    return str(index) + '_' + str(cluster_number)
