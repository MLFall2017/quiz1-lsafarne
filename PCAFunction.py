import numpy as np
import pandas as pd
from numpy import linalg as la
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
    print(np.cov(mean_cent_data[:,0],mean_cent_data[:,1]))
    print(cov_data)
    # -------------------Step 4: Computing Eigenvalues and EigenVectors-----------
    eig_vals, eig_vec = la.eig(cov_data)
    print("eigvalues is {}".format(eig_vals))
    print("eigenVectors is {}".format(eig_vec))

    # ------------------Step 5: Sorting Eigenvalues----------------------
    eig_val_vec = [(eig_vals[i], eig_vec[:, i]) for i in range(len(eig_vals))]

    eig_val_vec.sort(key=lambda x: x[0], reverse=True)
    temp=[]
    j=1
    for i in eig_val_vec:
        if j<=k:
            temp.append(i[1])
            j+=1
        else:
            break

    transform=np.array(temp)
    print(transform)
   # transform2=np.transpose(transform)
    return transform.T
