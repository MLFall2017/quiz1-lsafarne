import numpy as np
import pandas as pd
from numpy import linalg as la
from PCAFunction import pca
#---------------------Read the Dataset-------------------------
dataSet = pd.read_csv('dataset_1.csv')
dataSet=dataSet.values
#--------------------------------------------
k=2 #number of principal components to keep
pcaMatrix=pca(dataSet,k)
y=np.matmul(dataSet,pcaMatrix)
print(y)
