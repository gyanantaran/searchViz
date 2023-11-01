#!/usr/bin/env python

from .constants import (
    N_X_DISTRIBUTION,
    N_Y_DISTRIBUTION,
    colors,
    EDGE_CONFIDENCE,
    NODE_RADIUS,
)

from numpy import arange, full, uint8, random, column_stack, zeros, triu_indices
import time

from ._typing import NodeType, NodeList, NodeLocs, NodeCount
from .Node import Node

import threading


class Graph:
    def __init__(self, n: NodeCount | int):
        self.N_num = n

        _start_time = time.time()

        # Node stuff
        self.N = arange(0, self.N_num, dtype=NodeCount)
        self.N_locs = create_nodes(
            NodeCount(self.N_num)
        )  # for typecasting int to np.uint16

        self.N_colors = full((self.N_num, 4), colors["BLUE"], dtype=uint8)
        self.N_radii = full((self.N_num,), NODE_RADIUS, dtype=uint8)

        # start and end nodes
        start, goal = random.randint(0, self.N_num, size=2, dtype=NodeCount)
        self.start = start
        self.goal = goal

        self.N_colors[start] = colors["YELLOW"]
        self.N_colors[goal] = colors["RED"]

        self.N_radii[start] = 5 * NODE_RADIUS
        self.N_radii[goal] = 5 * NODE_RADIUS

        # Edge stuff
        self.edge_connections, self.edge_colors = create_edges(self.N_locs)

        # Search stuff
        self.open_ids, self.closed_ids = [], []

        _end_time = time.time()
        _elapsed_time = _end_time - _start_time

        print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

    ########################################################################
    #                   THE MOVEGEN AND GOALTEST FUNCTIONS
    ########################################################################

    def MoveGen(self, state: NodeType) -> NodeList:
        """
        Takes a state and returns an array of neighbors
        """
        neighbors = []

        id = 0
        while id < self.N_num:
            if (
                self.edge_connections[id, state]
                or self.edge_connections[state, id]
            ):
                neighbors.append(id)

            id += 1

        # print("neighbors", neighbors)
        # exit(0)

        # # updating the node-ui : will not work, as need to know closed for not re-entering node colors
        # for node in neighbors:
        #     id = node.id
        #     self.N_colors[id] = colors["BLUE"]
        #     self.N_radii[id] = 2 * NODE_RADIUS

        return neighbors

    def GoalTest(self, state: NodeType) -> bool:
        foundGoal = state == self.goal

        # # updating the node-ui
        # self.N_colors[id] = colors["RED"]
        # self.N_radii[id] = 2 * NODE_RADIUS

        return foundGoal

    def update_nodes(self):
        self.N_colors[self.open_ids] = colors["BLUE"]
        self.N_radii[self.open_ids] = 2 * NODE_RADIUS

        for id in self.closed_ids:
            self.N_colors[id] = colors["RED"]
            self.N_radii[id] = 1.5 * NODE_RADIUS

        return


def create_nodes(n: NodeCount) -> NodeLocs:
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
    x_values = N_X_DISTRIBUTION(int(n))
    y_values = N_Y_DISTRIBUTION(int(n))

    node_locs = column_stack((x_values, y_values))

    print("✅\tFinished creating nodes!\n")

    return node_locs


def create_edges(nodes: NodeLocs):
    """
    Creates edges for the give nodes locations
    """
    # TODO: need to seperate the threading or remove the animation
    global done
    done = threading.Event()

    dot_thread = threading.Thread(target=animate_dots)
    dot_thread.start()

    n = len(nodes)
    edge_connections = zeros((n, n))
    i, j = triu_indices(n, k=1)  # only one way edges

    _toss = random.rand(n, n)
    _confidence = zeros((n, n))
    _confidence[i, j] = EDGE_CONFIDENCE(nodes[i], nodes[j])

    # confidence number of times there will be an edge
    edge_connections = _toss <= _confidence
    edge_colors = full((n, 4), fill_value=colors["WHITE"], dtype=uint8)

    # Stop the dot animation
    done.set()
    dot_thread.join()  # Wait for the animation thread to finish

    print("\n✅\tFinished creating edges!\n")
    return edge_connections, edge_colors


# for animating while the edges get created
def animate_dots():
    symbols = [".", "..", "...", "...🐌"]
    while not done.is_set():
        for symbol in symbols:
            print(f"🕰️\tCreating edges {symbol}", end=" \r", flush=True)
            time.sleep(0.25)
    return
