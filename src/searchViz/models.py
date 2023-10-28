#!/usr/bin/env python3

# contains the models for edges and nodes

import numpy as np
from typing import Callable
from numpy.typing import NDArray

# TODO: because of circular import issues
NodeLocs = NDArray[np.float64]


# distribution of nodes
def N_Distbn(length: int, model: str) -> Callable[[int], NodeLocs]:
    """Return a function to generate a distribution given number of nodes"""

    def nodes_uniform(n: int) -> NDArray[np.float64]:
        # return np.random.normal(length / 2, length / 5, n)
        return np.random.uniform(0, length, n)

    def nodes_gaussian(n: int) -> NDArray[np.float64]:
        return np.random.normal(length / 2, length / 5, n)
        # return np.random.uniform(0, length, n)

    return nodes_gaussian if model == "gaussian" else nodes_uniform


def E_Distbn(
    max_len: float, min_len: float, model: str
) -> Callable[[NodeLocs, NodeLocs], NDArray[np.float64]]:
    """Return a function to generate a edge distribution given"""

    def edge_thresh(node1: NodeLocs, node2: NodeLocs) -> NDArray[np.float64]:
        distance = np.linalg.norm(node1 - node2, axis=1)
        return (min_len <= distance) & (distance <= max_len)

    def edge_exp(node1: NodeLocs, node2: NodeLocs) -> NDArray[np.float64]:
        # Return probability of edge based on distance between the nodes

        # Temp calculations for lambda value
        x0 = max_len
        y0 = 0.06
        lam = -1 * np.log(y0) / x0

        distance = np.linalg.norm(node1 - node2, axis=1)
        val = -lam * distance

        # Calculate probability using the exp function
        prob = np.exp(val)

        return prob

    return edge_exp if model == "exponential" else edge_thresh
