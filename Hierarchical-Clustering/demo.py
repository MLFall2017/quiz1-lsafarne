import pandas as pd
import HierarchicalClusteringAlg as hc
import util
import numpy as np
dataset=pd.read_csv('toyDataset.csv')
dset=dataset.values
#print(dset.shape[0])
#clusters=hc.initialize(dset)
#print(clusters[0][0])
#print(clusters[1])
#dist_dic=hc.clusters_dist(clusters)
#print(len(dist_dic))
#for i in dist_dic:
#    print(clusters[i[0]],clusters[i[1]],i,dist_dic[i])
#closest_clusters=util.min_sequence(dist_dic)
#test=[]
#print(clusters[closest_clusters["min_key"][1]])
#for i in closest_clusters["min_key"]:
#    for j in clusters[i]:
#        test.append(j)
#print(test)
#hc.mearge_clusters(clusters,0,dist_dic)
clusters=hc.hierarchical_clustering(dset, 2.1, "complete")
for i in clusters:
    print(i)

#clusters=[[np.array([4, 3]), np.array([5, 4])], [np.array([2, 1]), np.array([1, 1])], [np.array([5, 4])], [np.array([1, 4])], [np.array([2, 6])]]
#print(len(clusters))
#dist_dict=hc.clusters_dist(clusters)
#print(dist_dict)





