import numpy as np
import pandas as pd
X=np.arange(0.0,10,0.1)
Y=5*X
noise=np.random.normal(0,0.1,len(X))
YNew=Y+noise
corrXYnew=np.corrcoef(YNew,X)
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(2, 1, 1)
ax.scatter(YNew,X, color='green')
plt.show()
##################################################
dataset=pd.read_csv('C:\\Users\\lsafarne\\dataset_1.csv')
print(dataset.size)





