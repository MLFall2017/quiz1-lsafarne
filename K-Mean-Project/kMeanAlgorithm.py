import numpy as np
import util


def closetCluster(centroids, instance):
    """Find the closest cluster to an instance using the distance between the distance and centroids"""
    minDist = util.distance(centroids[0], instance)
    result = 0
    i = 1
    while i < len(centroids):
        if util.distance(centroids[i], instance) < minDist:
            minDist = util.distance(centroids[i], instance)
            result = i
        i += 1

    return result


def kMean(dtset, k, iter):
    """K-Means algorithm
    :type dtset np.array
    :type meanRangeVals dictionary
    :type centroids dictionary
    :type clusters dictionary
    k number of clusters
    """
    # -----------------Initialization--------------------
    meanRangeVals = util.mean_range(dtset)
    #centroids = util.centroidGenerator(meanRangeVals, k)
    centroids = util.centroid_pick(dtset,k)

    result = {}
    numFeatures = dtset.shape[1]

    # ---------------Iterations-------------------------
    for i in range(iter):
        clusters = {}
        for x in range(k):
            clusters[x] = []
        for j in range(dtset.shape[0]):  # Assign an instance to the closest cluster
            clusters[closetCluster(centroids, dtset[j, :])].append(dtset[j, :])
        for d in range(k):  # Update centroids
            if len(clusters[d]) > 0:
                mean_cluster = util.nDMean(clusters[d], numFeatures)
                if len(mean_cluster) == dtset.shape[1]:
                    centroids[d] = mean_cluster
                else:  # if mean_cluster is empty, i.e. there is not point in the cluster
                    pass;
                print("d is {} and cluster is{} and type is {}".format(d, len(clusters[d]), type(clusters[d])))

    for key, cluster in clusters.items():
        print(str(key) + " " + str(len(cluster)))
        print(cluster)
    result["clusters"] = clusters
    result["centroids"] = centroids
    return result
