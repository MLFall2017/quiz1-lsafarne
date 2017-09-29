import numpy as np
import pandas as pd
from numpy import linalg as la
import math
def pca(dataSet,k):
    """Principal Component analysis"""
    # --------------------Step 1: Computing the Mean of Each Random Variable-------------

    mean_vec = []
    num_v = dataSet.shape[1]  # number of random variables
    for i in range(num_v):
        mean_vec.append(np.mean(dataSet[:, i]))
    print("mean vector {}:".format(mean_vec))
    # -------------------Step 2: Mean-centering Random Variables-----------------
    mean_cent_data = dataSet
    for i in range(num_v):
        mean_cent_data[:, i] = dataSet[:, i] - mean_vec[i]
    print(mean_cent_data.shape)
    # -------------------Step 3: Computing Covariance Matrix---------------------
    cov_data = np.cov(mean_cent_data.T)
    stan = mean_cent_data
    for i in range(num_v):
        stan[:,i]=stan[:,i]/math.sqrt(cov_data[i,i])
    print(stan.shape)
    cov_dataNew=np.cov(mean_cent_data.T)
    print("Covariance matrix is: {}".format(cov_data.shape))
    print("Variance of x: {}".format(cov_data[0,0]))
    print("Covariance matrix for x,y: {}".format(np.cov(mean_cent_data[:,0],mean_cent_data[:,1])))
    #print("Covariance matrix for y,z: {}".format(np.cov(mean_cent_data[:,1],mean_cent_data[:,2])))
    totalVar=0
    for i in range(49):
        totalVar=totalVar+cov_data[i,i]
    print("totalVar origin {}".format(totalVar))

    # -------------------Step 4: Computing Eigenvalues and EigenVectors-----------
    eig_vals, eig_vec = la.eig(cov_data)
    #print("eigvalues are {}".format(eig_vals))
    totalVarPCA=0
    for i in range(49):
        totalVarPCA=totalVarPCA+eig_vals[i]
    print("totalVarPCA {}".format(totalVar))

   # print("eigenVectors are {}".format(eig_vec))

    # ------------------Step 5: Sorting Eigenvalues----------------------
    eig_val_vec = [(eig_vals[i], eig_vec[:, i]) for i in range(len(eig_vals))]

    eig_val_vec.sort(key=lambda x: x[0], reverse=True)
    print("eig_val_vec {}".format(eig_val_vec))
    eig_vals=np.array([i[0] for i in eig_val_vec]) #Sorted eigen values
    temp=[]
    j=1
    for i in eig_val_vec:
        if j<=k:
            temp.append(i[1])
            j+=1
        else:
            break
    print("temp {}".format(temp))
    pcaMatrix=np.array(temp)
    pcaMatrix=pcaMatrix.T
    pcaScores=np.matmul(dataSet,pcaMatrix)
    pcaResults={'eigenValues':eig_vals, 'pcaMatrix':pcaMatrix, 'pcaScores':pcaScores}
    print("Result matrix is:{}".format(pcaMatrix))
   # transform2=np.transpose(transform)
    return pcaResults
