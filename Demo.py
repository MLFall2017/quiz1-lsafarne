import numpy as np
import pandas as pd
from numpy import linalg as la
from PCAFunction import pca
import visualizeData as VID
#---------------------Read the Dataset-------------------------
#dataSet = pd.read_csv('dataset_1.csv')
#--------------------------------------------PCA for Quiz 1-------------------
#k=3 #number of principal components to keep
#pcaMatrix=pca(dataSet,k)
#pcaScores=np.matmul(dataSet,pcaMatrix)
#print("new components {}".format(pcaScores))
#---------------------------------------------PCA sample data--------------
#x1 = np.arange(start=0, stop=20, step=0.1)
#x2 = 2 * x1 + np.random.normal(loc=0, scale=0.5,size=len(x1))  # loc=Mean, scale=standard deviation, size=number of sample to generate
#dataForAnalysis=np.column_stack((x1,x2))
#VID.visualizeRaw(x1, x2)
#-------------------------------------------PCA Quiz2----------------------------------
dataSet = pd.read_csv('SCLC_study_output_filtered.csv')
dataSet=dataSet.values
dataSet=dataSet
print("shape of dataSet {}".format(dataSet.shape))
k=49
pcaResults=pca(dataSet,k)
eigenValues=pcaResults['eigenValues']
print("eigenValues {}".format(eigenValues))
print("size {}".format(eigenValues.size))
pcaMatrix=pcaResults['pcaMatrix']
VID.screeplot(eigenValues,k)
scores=pcaResults['pcaScores']
print(scores)
VID.scorePlot(scores)
VID.loadingPlot(pcaMatrix)
reconstructedData=np.matmul(scores,pcaMatrix.T)
VID.visualizeRaw(reconstructedData[:,0], reconstructedData[:,1])
