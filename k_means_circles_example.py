# Project: Temp
# File name: Dan
# Descriptions: 
# Author: Hanting Xie
# Date created: 08/11/2016
# Date last modified: 08/11/2016
# Python version: 2.7

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import make_circles



X, y = make_circles(n_samples=1000, factor=.3, noise=.05)

y_fit = KMeans(n_clusters=2).fit(X)

reds = y_fit.labels_ == 0
blues = y_fit.labels_ == 1

plt.plot(X[reds, 0], X[reds, 1], "ro")
plt.plot(X[blues, 0], X[blues, 1], "bo")

plt.show()