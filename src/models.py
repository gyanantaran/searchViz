#!/usr/bin/env python3

# contains the models for edges and nodes

import numpy as np


# distribution of nodes
def nodes_dist_wrapper(length: int, model: str):
    def nodes_uniform(n: int):
        # return np.random.normal(length / 2, length / 5, n)
        return np.random.uniform(0, length, n)

    def nodes_gaussian(n: int):
        return np.random.normal(length / 2, length / 5, n)
        # return np.random.uniform(0, length, n)

    return nodes_gaussian if model == "gaussian" else nodes_uniform


def edge_dist_wrapper(max_edge_len: float, min_edge_len: float, model: str):
    def edge_threshold(node1: np.ndarray, node2: np.ndarray) -> int:
        distance = np.linalg.norm(node1 - node2, axis=1)
        return (min_edge_len <= distance) & (distance <= max_edge_len)

    def edge_exp(node1: np.ndarray, node2: np.ndarray) -> float:
        # Return probability of edge based on distance between the nodes

        # Temp calculations for lambda value
        x0 = max_edge_len
        y0 = 0.1
        lam = -1 * np.log(y0) / x0

        distance = np.linalg.norm(node1 - node2, axis=1)
        val = -lam * distance

        # Calculate probability using the exp function
        prob = np.exp(val)

        return prob

    return edge_exp if model == "exponential" else edge_threshold
