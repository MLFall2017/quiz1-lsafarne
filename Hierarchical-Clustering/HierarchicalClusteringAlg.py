import util


def initialize(dset):
    """
    Initialize clusters
    :type dset: np.array
    """
    clusters = [[] for i in range(dset.shape[0])]

    for i in range(dset.shape[0]):
        clusters[i].append(dset[i][:])
    return clusters


def single_clusters_dist(cluster1, cluster2):
    """
    Compute pairwise distance btw clusters and pick the smallest distance (single linkage)
    :param cluster1: list
    :param cluster2: list
    :return min_dist: float
    """
    min_dist = util.distance(cluster1[0], cluster2[0])
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            temp = util.distance(cluster1[i], cluster2[j])
            if min_dist > temp:
                min_dist = temp

    return min_dist


def complete_cluster_dist(cluster1, cluster2):
    """
    Compute pairwise distance btw clusters and pick the greatest distance (complete linkage)
    :param cluster1: list
    :param cluster2: list
    :return: max_dist: float
    """
    max_dist = util.distance(cluster1[0], cluster2[0])
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            temp = util.distance(cluster1[i], cluster2[j])
            if max_dist < temp:
                max_dist = temp

    return max_dist


def mean_cluster(cluster):
    """
    :param cluster: list
    :return: result:
    """
    result = []
    temp1 = 0
    temp2 = 0
    for i in cluster:
        temp1 += i[0]
        temp2 += i[1]
    result = [temp1 / len(cluster), temp2 / len(cluster)]
    return result


def centroid_cluster_dist(cluster1, cluster2):
    """
    Find the centroid in a cluster
    :param cluster1: list
    :param cluster2: list
    :return:
    """
    mean1 = mean_cluster(cluster1)
    mean2 = mean_cluster(cluster2)
    return util.distance(mean1, mean2)


def average_cluster_dist(cluster1, cluster2):
    """
    Compute pairwise distances and return their average
    :param cluster1:
    :param cluster2:
    :return: average_dist:
    """
    temp = 0
    for i in range(len(cluster1)):
        for j in range(len(cluster2)):
            temp += util.distance(cluster1[i], cluster2[j])
    average_dist = temp / (len(cluster1) * len(cluster2))

    return average_dist


def clusters_dist(clusters, linkage):
    """
    Create a dictionary from distances btw every two clusters
    :param clusters: list
    :param linkage: string
    :return: dist_dic
    """
    dist_dic = {}
    if linkage == "single":
        for i in range(0, len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist_dic[(i, j)] = dist_dic[(j, i)] = single_clusters_dist(clusters[i], clusters[j])
    if linkage == "complete":
        for i in range(0, len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist_dic[(i, j)] = dist_dic[(j, i)] = complete_cluster_dist(clusters[i], clusters[j])
    if linkage == "centroid":
        for i in range(0, len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist_dic[(i, j)] = dist_dic[(j, i)] = centroid_cluster_dist(clusters[i], clusters[j])
    if linkage == "average":
        for i in range(0, len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist_dic[(i, j)] = dist_dic[(j, i)] = average_cluster_dist(clusters[i], clusters[j])

    return dist_dic


def merge_clusters(old_clusters, closest_clusters):
    """
    Merge closets clusters
    :param old_clusters: list
    :param closest_clusters: list
    :return: new_clusters: list
    """
    new_clusters = []
    temp = []
    for i in closest_clusters["min_key"]:
        for j in old_clusters[i]:
            temp.append(j)

    new_clusters.insert(0, temp)
    if closest_clusters["min_key"][1] < closest_clusters["min_key"][0]:
        del old_clusters[closest_clusters["min_key"][0]]
        del old_clusters[closest_clusters["min_key"][1]]
    else:
        del old_clusters[closest_clusters["min_key"][1]]
        del old_clusters[closest_clusters["min_key"][0]]

    for i in old_clusters:
        new_clusters.append(i)

    return new_clusters


def hierarchical_clustering(dset, threshold, linkage):
    clusters = []
    if len(dset) > 0:  # if the dset is not empty
        clusters = initialize(dset)
        dist_dict = clusters_dist(clusters, linkage)  # find the distance btw clusters
        closest_clusters = util.min_sequence(dist_dict)  # find the two clusters with min distance
        while len(closest_clusters) > 0 and closest_clusters["min_val"] < threshold and \
                len(clusters) > 1:  # While the min_val is less than the threshold continue merging
            clusters = merge_clusters(clusters, closest_clusters)
            dist_dict = clusters_dist(clusters, linkage)
            closest_clusters = util.min_sequence(dist_dict)
    return clusters
