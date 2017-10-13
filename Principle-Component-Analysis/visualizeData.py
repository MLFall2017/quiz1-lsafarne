import numpy as np
import matplotlib
from matplotlib import pyplot as plt
def visualizeRaw(x1, x2):
    """Visualize the raw data"""
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(x1,x2,color='blue')
    #ax.set_aspect('equal','box')
    plt.show()

#------------------------------Scree Plot--------------------#
def screeplot (eigenValues,k):

    """Displays the number of the principle component
        versus its corresponding eigenvalue"""

    temp=[i for i in range(len(eigenValues))]
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title('scree plot')
    #ax.set_aspect('equal', 'box')
    ax.scatter(range(len(eigenValues)),eigenValues)
    #plt.xlim(-0.5, 5)
    #plt.ylim(-0.5, 5)
    plt.show()

def scorePlot(scores):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title('score plot')
    #ax.set_aspect('equal', 'box')
    ax.scatter(scores[:, 0], scores[:, 1])
    #plt.xlim(-20,20)
    #plt.ylim(-6,6)
    plt.show()
def score_color_plot(scores):
    fig=plt.figure()
    plt.scatter(scores[0:21, 0], scores[0:21, 1],hold=True,marker='o',c='r')
    plt.scatter(scores[21:41, 0], scores[21:41, 1],hold=True,marker='o',c='b')
    plt.show()

def loadingPlot(pcaMatrix):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_title("loading Plot")
    #ax.set_aspect('equal','box')
    ax.scatter(pcaMatrix[:,0],pcaMatrix[:,1])
    #plt.xlim(-10,10)
    #plt.ylim(-10,10)
    plt.show()