#!/usr/bin/env python

from .constants import NODES_X_DISTRIBUTION, NODES_Y_DISTRIBUTION
from .constants import EDGE_CONFIDENCE, RED, BLUE, NODE_RADIUS

import numpy as np
import time
from typing import List

import threading


class Node:
    def __init__(self, id: np.uint16):
        """
        id: the id of the node, np.uint16 for maximum
            of 2^16 (= 65535 + 1) nodes on the screen
        """
        self.id = id


class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes

        _start_time = time.time()
        self.nodes, self.colors, self.radius = create_nodes(num_nodes)
        self.edges, self.edge_colors = create_edges(self.nodes)

        start_id, end_id = np.random.randint(0, self.num_nodes, size=2, dtype=np.uint16)
        self.start_node = Node(start_id)
        self.end_node = Node(end_id)

        _end_time = time.time()
        _elapsed_time = _end_time - _start_time

        print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

    ########################################################################
    #                   THE MOVEGEN AND GOALTEST FUNCTIONS
    ########################################################################

    def moveGen(self, state: Node) -> List[Node]:
        """
        Takes a state and returns an array of neighbors
        """
        neighbors = []

        id = np.uint16(0)
        while id < self.num_nodes:
            if [id, state.id] == 1:
                neighbors.append(Node(id))
            id += 1

        print()
        return neighbors

    def goalTest(self, state: Node) -> bool:
        print(state)
        return True


def create_nodes(n: int):
    """
    Returns a vector of `n` points, colors, radii:
    [
      (5.0, 0.1)
      (2.1, 5.0)
          ...
      (3.1, 4.0)
    ]
    according to a distribution function defined in constants
    """

    print(f"🕰️\tCreating {n} nodes... timer started...")
    x_values = NODES_X_DISTRIBUTION(n)
    y_values = NODES_Y_DISTRIBUTION(n)

    colors = np.full((n, 4), fill_value=BLUE, dtype=np.uint8)
    radii = np.full((n,), fill_value=NODE_RADIUS, dtype=np.uint8)

    # generating the goal node
    goal_loc = np.random.randint(0, n, 1)
    colors[goal_loc] = RED
    radii[goal_loc] = 3 * NODE_RADIUS

    nodes = np.column_stack((x_values, y_values))
    print("✅\tFinished creating nodes!\n")

    return nodes, colors, radii


def create_edges(nodes: np.ndarray):
    """
    Creates edges for the give nodes locations
    """
    global done
    done = threading.Event()

    dot_thread = threading.Thread(target=animate_dots)
    dot_thread.start()

    n = len(nodes)
    edges = np.zeros((n, n))
    i, j = np.triu_indices(n, k=1)

    _toss = np.random.rand(n, n)
    _confidence = np.zeros((n, n))
    _confidence[i, j] = EDGE_CONFIDENCE(nodes[i], nodes[j])

    # confidence number of times there will be an edge
    edges = _toss <= _confidence
    edge_color = (edges).astype(int)

    # Stop the dot animation
    done.set()
    dot_thread.join()  # Wait for the animation thread to finish

    print("\n✅\tFinished creating edges!\n")
    return edges, edge_color


# for animating while the edges get created
def animate_dots():
    symbols = [".", "..", "...", "...🐌"]
    while not done.is_set():
        for symbol in symbols:
            print(f"🕰️\tCreating edges {symbol}", end=" \r", flush=True)
            time.sleep(0.25)
    return
