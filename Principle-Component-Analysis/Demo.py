import numpy as np
import pandas as pd
from numpy import linalg as la
import PCAFunction as pcaf
import visualizeData as VID
#---------------------Read the Dataset-------------------------
#dataSet = pd.read_csv('dataset_1.csv')
#dataSet=dataSet.values
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
#print("shape of dataSet {}".format(dataSet.shape))
cov_matrix=np.cov(dataSet,rowvar=False)

k=dataSet.shape[1]
pcaResults=pcaf.pca(dataSet,k)
eigenValues=pcaResults['eigenValues']
print("eigenValues {}".format(eigenValues))
#print("size {}".format(eigenValues.size))
pcaMatrix=pcaResults['pcaMatrix']
#VID.screeplot(eigenValues,k)
scores=pcaResults['pcaScores']
#print(scores)
VID.scorePlot(scores)
#VID.loadingPlot(pcaMatrix)
reconstructedData=np.matmul(scores,pcaMatrix.T)
#VID.visualizeRaw(reconstructedData[:,0], reconstructedData[:,1])
VID.score_color_plot(scores)
keep_pca=pcaf.pca_to_keep(eigenValues,0.75)
print(keep_pca,(eigenValues[0]+eigenValues[1]+eigenValues[2]+eigenValues[3])/sum(eigenValues))
sum_cov=pcaf.total_var(cov_matrix)
print(sum_cov)
sum_pca_var=sum(eigenValues)
print(sum_pca_var)
cov_pca=np.cov(pcaMatrix,rowvar=False)
print(cov_pca[0][1],)
standardData=pcaf.standardize(dataSet)
cov_stand_matrix=np.cov(standardData, rowvar=False)
print(cov_stand_matrix.shape[0])
sum_standard=pcaf.total_var(cov_stand_matrix)
print(sum_standard)


