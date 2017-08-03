# coding=utf-8

"""
http://scikit-learn.org/stable/tutorial/statistical_inference/unsupervised_learning.html#
http://www.cnblogs.com/leoo2sk/archive/2010/09/20/k-means.html
http://sports.sina.com.cn/csl/table/?cre=360.ala.zc.sc&dpc=1
"""

from sklearn import cluster, datasets
import numpy as np

# fb_data = np.array([[1., 1., 0.5],
#                     [0.3, 0., 0.19],
#                     [0., 0.15, 0.13],
#                     [0.24, 0.76, 0.25],
#                     [0.3, 0.76, 0.06],
#                     [1., 1., 0.],
#                     [1., 0.76, 0.5],
#                     [1., 0.76, 0.5],
#                     [0.7, 0.76, 0.25],
#                     [1., 1., 0.5],
#                     [1., 1., 0.25],
#                     [1., 1., 0.5],
#                     [0.7, 0.76, 0.5],
#                     [0.7, 0.68, 1.],
#                     [1., 1., 0.5]])

# fb_data = np.array([[41], [40], [35], [34], [31], [30], [29], [27], [23], [22], [21], [18], [17], [16], [15], [10]])

fb_data = np.array([
    [13, 2, 4, 41, 27],
    [12, 4, 3, 46, 21],
    [10, 5, 4, 29, 20],
    [10, 4, 4, 31, 18],
    [9, 4, 6, 27, 24],
    [8, 6, 5, 36, 29],
    [8, 5, 6, 31, 25],
    [7, 6, 6, 27, 25],
    [6, 5, 7, 35, 29],
    [6, 4, 9, 24, 29],
    [5, 6, 7, 20, 26],
    [4, 7, 8, 20, 27],
    [3, 8, 8, 22, 28],
    [4, 4, 11, 21, 43],
    [3, 6, 9, 12, 26],
    [2, 4, 13, 14, 39]]
)

# print fb_data.ndim
k_means = cluster.KMeans(n_clusters=5)
k_means.fit(fb_data)
print k_means.labels_
