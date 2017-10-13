from sklearn.cluster import k_means
from sklearn.cluster import KMeans
from sklearn import datasets

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
feature_names = iris.feature_names
y = iris.target
target_names = iris.target_names
fig = plt.figure(figsize=(10, 8))
#############################################Setal Length and Width#########################
ax = fig.add_subplot(2, 1, 1)
#------------------Setosa-----------------
II = (y==0)
ax.scatter(X[II,0], X[II, 1], color='blue')
#----------------Versicolour-----------
II = (y==1)
ax.scatter(X[II,0], X[II, 1], color='red')
#---------------Virginica
II = (y==2)
ax.scatter(X[II,0], X[II, 1], color='green')
ax.set_title('sepal')
ax.set_xlabel('length')
ax.set_ylabel('width')
##########################################Petal Length and Width####################
ax = fig.add_subplot(2, 1, 2)
II = (y==0)
ax.scatter(X[II,2], X[II, 3], color='blue')
II = (y==1)
ax.scatter(X[II,2], X[II, 3], color='red')
II = (y==2)
ax.scatter(X[II,2], X[II, 3], color='green')
ax.set_title('petal')
ax.set_xlabel('length')
ax.set_ylabel('width')
fig.show()