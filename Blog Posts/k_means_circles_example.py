import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import make_circles

X, y = make_circles(n_samples=10000, factor=.3, noise=.07)
y_fit = KMeans(n_clusters=2).fit(X)

plt.figure(1)
plt.subplot(221)

reds = y == 0
blues = y == 1
plt.plot(X[reds, 0], X[reds, 1], "ro")
plt.plot(X[blues, 0], X[blues, 1], "bo")
plt.title('Its so Raw')
plt.subplot(222)

reds = y_fit.labels_ == 0
blues = y_fit.labels_ == 1
plt.plot(X[reds, 0], X[reds, 1], "ro")
plt.plot(X[blues, 0], X[blues, 1], "bo")
plt.title('K-means done fucked it')
plt.show();