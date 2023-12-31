#!/usr/bin/env python3

# contains the models for edges and nodes

from typing import Callable

from numpy import exp, float64, linalg, log, random
from numpy.typing import NDArray

# TODO: because of circular import issues
NodeLocs = NDArray[float64]


# distribution of nodes
def N_Distbn(length: int, model: str) -> Callable[[int], NodeLocs]:
    """Return a function to generate a distribution given number of nodes"""

    def nodes_uniform(n: int) -> NDArray[float64]:
        # return random.normal(length / 2, length / 5, n)
        return random.uniform(0, length, n)

    def nodes_gaussian(n: int) -> NDArray[float64]:
        return random.normal(length / 2, length / 5, n)
        # return random.uniform(0, length, n)

    return nodes_gaussian if model == "gaussian" else nodes_uniform


def E_Distbn(
    max_len: float, min_len: float, model: str
) -> Callable[[NodeLocs, NodeLocs], NDArray[float64]]:
    """Return a function to generate a edge distribution given"""

    def edge_thresh(node1: NodeLocs, node2: NodeLocs) -> NDArray[float64]:
        distance = linalg.norm(node1 - node2, axis=1)
        return (min_len <= distance) & (distance <= max_len)

    def edge_exp(node1: NodeLocs, node2: NodeLocs) -> NDArray[float64]:
        # Return probability of edge based on distance between the nodes

        # Temp calculations for lambda value
        x0 = max_len
        y0 = 0.06
        lam = -1 * log(y0) / x0

        distance = linalg.norm(node1 - node2, axis=1)
        val = -lam * distance

        # Calculate probability using the exp function
        prob = exp(val)

        return prob

    return edge_exp if model == "exponential" else edge_thresh
