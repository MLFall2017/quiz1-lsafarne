import numpy as np
from sklearn import datasets
from sklearn.cluster import k_means
from sklearn.cluster import KMeans
import util
import kMeanAlgorithm as km
import pandas as pd
#---------------------------------------iris dataset---------------------
#irisData=datasets.load_iris()  #irisData is the type of <class 'sklearn.utils.Bunch'>
#dtset=irisData.data
# dtset has numpy array datatype with size 150*4.
#Each row of dtset is a sample. Each column represents a feature:
# Sepal Length, Sepal Width, Petal Length and Petal Width.
#---------------------------------------SCLC_study_output_filtered_2.csv-------------
dtset = pd.read_csv('SCLC_study_output_filtered_2_new.csv')
dtset=dtset.values
meanRVals=util.mean_range(dtset)
print(meanRVals)
temp=util.centroidGenerator(meanRVals,2)
print(temp)
result=km.kMean(dtset,2,1)
print("Centroid")
print(result["centroids"])