# In a dataset, columns correspond features, and rows represent samples

import math
import numpy as np


def mean_range(dtset):

    """Find mean and range of every feature"""

    result = {}
    for i in range(dtset.shape[1]):
        result[i] = {"mean": dtset[:, i].mean(), "range": dtset[:, i].std()}
    return result



def distance(p1, p2):
    """Compute Euclidean Distance btw two points"""

    temp = 0
    for i in range(len(p1)):
        temp += math.pow(p1[i] - p2[i], 2)
    result = math.sqrt(temp)
    return result



def centroidGenerator(meanRangeVals, k):
    """Generate k number of centroids using the mean and std values of features"""

    centroids = {}
    for i in range(k):
        centroids[i] = np.array(
            [np.random.normal(loc=meanRangeVals[j]["mean"], scale=meanRangeVals[j]["range"]) for j in
             range(len(meanRangeVals))])
            #meanRangeVals[j]["mean"]


    return centroids

def centroid_pick(dset,k):
    upper=dset.shape[0]
    rand_indices=np.random.randint(low=0,high=upper, size=k)
    centroids={}
    j=0
    for i in rand_indices:
        centroids[j]=dset[i,:]
        j+=1
    return centroids






def nDMean(cluster,dim):
    """Find the Mean of points in a n-D space"""
    result = []
    try:
        for i in range(dim):
            result.append(np.mean(cluster[:][i]))
    except IndexError:
        print("result is {}".format(result))


    return np.array(result)
