import numpy as np


def vectorized_func(nodes):
    num_nodes = len(nodes)
    i, j = np.triu_indices(num_nodes, k=1)
    result = np.zeros((num_nodes, num_nodes))
    result[i, j] = nodes[i] * nodes[j]
    return result


nodes = np.array([1, 2, 3, 4, 5])
result = vectorized_func(nodes)
print(result)
