#!/usr/bin/env python

from .constants import NODES_X_DISTRIBUTION, NODES_Y_DISTRIBUTION
from .constants import EDGE_CONFIDENCE

import numpy as np


def x_distribution(n: int):
    return NODES_X_DISTRIBUTION(n)


def y_distribution(n: int):
    return NODES_Y_DISTRIBUTION(n)


def edge_confidence(node1: np.ndarray, node2: np.ndarray):
    return EDGE_CONFIDENCE(node1, node2)


def nodes(n: int):
    # returns a vector of `n` points:
    # [
    #   (5.0, 0.1)
    #   (2.1, 5.0)
    #       ...
    #   (3.1, 4.0)
    # ]
    # according to a distribution function defined in constants
    x_values = x_distribution(n)
    y_values = y_distribution(n)
    nodes = np.column_stack((x_values, y_values))

    return nodes


def edges(nodes: np.ndarray):
    n = len(nodes)
    edges = np.zeros((n, n))
    i, j = np.triu_indices(n, k=1)

    _toss = np.random.rand(n, n)
    _confidence = np.zeros((n, n))
    _confidence[i, j] = edge_confidence(nodes[i], nodes[j])

    # confidence number of times there will be an edge
    edges = _toss <= _confidence

    return edges
