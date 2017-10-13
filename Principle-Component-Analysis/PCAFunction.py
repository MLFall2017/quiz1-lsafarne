import numpy as np
import pandas as pd
from numpy import linalg as la
import math
def mean_centre(dataSet):
    mean_vec = np.mean(dataSet, axis=0)
    mean_cent_data = dataSet
    num_v = dataSet.shape[1]
    for i in range(num_v):
        mean_cent_data[:, i] = dataSet[:, i] - mean_vec[i]
    print(mean_cent_data.shape)
    return mean_cent_data

def standardize(dataSet):
    """ standardize a dataset"""
    mean_cent_data=mean_centre(dataSet)
    std_vec=np.std(dataSet,axis=0)
    result=dataSet
    for i in range(dataSet.shape[1]):
        result[:,i]=mean_cent_data[:,i]/std_vec[i]
    return result

def total_var(cov_matrix):
    result=0
    for i in range(cov_matrix.shape[0]):
        result+=cov_matrix[i][i]
    return result

def pca_to_keep(eigen_vals,precision):
    i=0
    total_variance=sum(eigen_vals)
    result=eigen_vals[0]
    while (result/total_variance)<precision:
        i+=1
        result+=eigen_vals[1]
    return i



def pca(dataSet,k):

    """
    Perform PCA
    :param dataSet:
    :param k:
    :return:
    """

    mean_cent_data=mean_centre(dataSet)
    cov_data = np.cov(mean_cent_data,rowvar=False)
    stan = standardize(dataSet)
    cov_stan=np.cov(stan,rowvar=False)
    print("cov_stan".format(cov_stan[0][0]))

    # -------------------Step 4: Computing Eigenvalues and EigenVectors-----------
    eig_vals, eig_vec = la.eig(cov_data)
    totalVarPCA=0
    for i in range(k):
        totalVarPCA=totalVarPCA+eig_vals[i]
    print("totalVarPCA {}".format(totalVarPCA))

    # ------------------Step 5: Sorting Eigenvalues----------------------
    eig_val_vec = [(eig_vals[i], eig_vec[:, i]) for i in range(len(eig_vals))]

    eig_val_vec.sort(key=lambda x: x[0], reverse=True)
    eig_vals=np.array([i[0] for i in eig_val_vec]) #Sorted eigen values
    temp=[]
    j=1
    for i in eig_val_vec:
        if j<=k:
            temp.append(i[1])
            j+=1
        else:
            break
    pcaMatrix=np.array(temp)
    pcaMatrix=pcaMatrix.T
    pcaScores=np.matmul(dataSet,pcaMatrix)
    pcaResults={'eigenValues':eig_vals, 'pcaMatrix':pcaMatrix, 'pcaScores':pcaScores}
   # transform2=np.transpose(transform)
    return pcaResults
