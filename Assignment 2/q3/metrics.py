import sklearn
import numpy as np

def adjusted_rand_index(labels, clusters):
    return sklearn.metrics.adjusted_rand_score(labels, clusters)

def adjusted_mutual_information(labels, clusters):
    return sklearn.metrics.adjusted_mutual_info_score(labels, clusters)

def purity_score(labels, clusters):
    contingency_matrix = sklearn.metrics.cluster.contingency_matrix(labels, clusters)
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)