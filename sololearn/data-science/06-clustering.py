import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from pandas.plotting import scatter_matrix
#calculate euclidean distance if numpy

x1 = np.array([0,1])
x2 = np.array([2,0])
euclidean = np.sqrt(((x1-x2)**2).sum())

#=========================
data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)

scatter_matrix(wine.iloc[:,[0,5]])
plt.show()