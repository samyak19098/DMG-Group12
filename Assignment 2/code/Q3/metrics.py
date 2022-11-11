import numpy as np
from sklearn import metrics

def adjusted_rand_index(labels, clusters):
    return metrics.adjusted_rand_score(labels, clusters)

def adjusted_mutual_information(labels, clusters):
    return metrics.adjusted_mutual_info_score(labels, clusters)

def purity_score(labels, clusters):
    contingency_matrix = metrics.cluster.contingency_matrix(labels, clusters)
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

def silhoutte_coefficient(X, clusters):
    return metrics.silhouette_score(X, clusters)

def calinski_harabasz_index(X, clusters):
    return metrics.calinski_harabasz_score(X, clusters)

def davies_bouldin_index(X, clusters):
    return metrics.davies_bouldin_score(X, clusters)