import numpy as np
import matplotlib
from matplotlib import pyplot as plt
def visualizeRaw(x1, x2):
    """Visualize the raw data"""
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1,facecolor='r')
    ax.scatter(x1,x2,color='blue')
    ax.set_aspect('equal','box')
    plt.show()

#------------------------------Scree Plot--------------------#
def screeplot (eigenValues,k):

    """Displays the number of the principle component
        versus its corresponding eigenvalue"""
    [i for i in range(k)]
    numberOfPca=np.arange(start=0,stop=k+1,step=1)
    temp=[]
    for i in range(len(eigenValues)):
        temp.append(i)
    tempArray=np.array(temp)
    print(tempArray.size)
    test=np.array([1,2])

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1,facecolor='r')
    ax.set_title('scree plot')
    ax.set_aspect('equal', 'box')
    ax.scatter(tempArray,eigenValues)
    plt.xlim(-20, 200)
    plt.ylim(-2, 200)
    plt.show()

def scorePlot(scores):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title('score plot')
    #ax.set_aspect('equal', 'box')
    ax.scatter(scores[:, 0], scores[:, 1])
    plt.xlim(-20,20)
    plt.ylim(-6,6)
    plt.show()

def loadingPlot(pcaMatrix):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title("loading Plot")
    #ax.set_aspect('equal','box')
    ax.scatter(pcaMatrix[:,0],pcaMatrix[:,1])
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.show()