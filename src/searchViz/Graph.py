#!/usr/bin/env python

from .constants import NODES_X_DISTRIBUTION, NODES_Y_DISTRIBUTION
from .constants import EDGE_CONFIDENCE, RED, BLUE, NODE_RADIUS

import numpy as np
import time


class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes

        _start_time = time.time()
        self.nodes, self.colors, self.radius = nodes(num_nodes)
        self.edges = edges(self.nodes)

        _end_time = time.time()
        _elapsed_time = _end_time - _start_time

        print(f"Took {_elapsed_time:.3f} seconds.")


def x_distribution(n: int):
    return NODES_X_DISTRIBUTION(n)


def y_distribution(n: int):
    return NODES_Y_DISTRIBUTION(n)


def edge_confidence(node1: np.ndarray, node2: np.ndarray):
    return EDGE_CONFIDENCE(node1, node2)


def nodes(n: int):
    # returns a vector of `n` points, colors:
    # [
    #   (5.0, 0.1)
    #   (2.1, 5.0)
    #       ...
    #   (3.1, 4.0)
    # ]
    # according to a distribution function defined in constants

    print("creating nodes... timer started...")
    x_values = x_distribution(n)
    y_values = y_distribution(n)

    colors = np.full((n, 4), fill_value=BLUE, dtype=np.uint8)
    radius = np.full((n,), fill_value=NODE_RADIUS, dtype=np.uint8)

    # generating the goal node
    goal_loc = np.random.randint(0, n, 1)
    colors[goal_loc] = RED
    print(goal_loc)
    radius[goal_loc] = 3 * NODE_RADIUS

    nodes = np.column_stack((x_values, y_values))
    print("Finished creating nodes!")

    return nodes, colors, radius


def edges(nodes: np.ndarray):
    print("creating edges...")

    n = len(nodes)
    edges = np.zeros((n, n))
    i, j = np.triu_indices(n, k=1)

    _toss = np.random.rand(n, n)
    _confidence = np.zeros((n, n))
    _confidence[i, j] = edge_confidence(nodes[i], nodes[j])

    # confidence number of times there will be an edge
    edges = _toss <= _confidence

    print("Finished creating edges!")

    return edges
