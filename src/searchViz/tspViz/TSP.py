# The travelling salesman problem

import numpy
from ..constants import NUM_NODES, colors

from ..graphViz.Graph import Graph
from .._typing import NodeCount

from numpy import zeros, random, arange, uint8, inf, linalg


class TSP(Graph):
    def __init__(self, n: NodeCount | int, name):
        super().__init__(n)
        self.name = name

        self.edge_connections = zeros((self.N_num, self.N_num))
        self.edge_colors = zeros((self.N_num, self.N_num, 4), dtype=uint8)

        self.all_cities = set(arange(0, self.N_num))
        self.visited_cities = set()

    def traverse(self):
        raise NotImplementedError


class ACO(TSP):
    def __init__(self, n: NodeCount | int = NUM_NODES):
        self.name = "ACO"
        super().__init__(n, name=self.name)

    def traverse(self):
        i = 0
        while i < 200:
            yield i
            i += 1
        return None


class Greedy(TSP):
    def __init__(self, n: NodeCount | int = NUM_NODES):
        self.name = "Greedy"
        super().__init__(n, name=self.name)

        self.start_node = random.randint(0, self.N_num)
        self.last_node = None

        self.cur_path = random.permutation(arange(0, self.N_num))

    def traverse(self):
        while len(self.visited_cities) < self.N_num:
            self.last_node = self.cur_node
            self.cur_node = self.nearest(self.cur_node)

            self.update_traversal(self.last_node, self.cur_node)
            self.visited_cities.add(self.cur_node)
            yield

    def nearest(self, cur_node):
        nearest_city = None
        min_dist = inf
        for city in self.remaining_cities:
            diff_vector = self.N_locs[city] - self.N_locs[cur_node]
            dist = linalg.norm(diff_vector)
            if dist < min_dist:
                print(dist)
                nearest_city = city
                min_dist = dist

        return nearest_city

    def update_traversal(self, last_node, cur_node):
        if last_node is not None and cur_node is not None:
            self.edge_connections[last_node, cur_node] = 1
            self.edge_connections[cur_node, last_node] = 1
            # self.edge_connections[] = 1

            self.edge_colors[last_node, cur_node] = colors["BRIGHT_WHITE"]
            self.edge_colors[cur_node, last_node] = colors["BRIGHT_WHITE"]

            self.N_colors[last_node] = colors["RED"]


class Random(TSP):
    def __init__(self, n: NodeCount | int = NUM_NODES):
        self.name = "Random"
        super().__init__(n, name=self.name)

        self.i = 0
        self.cur_path = random.permutation(arange(0, self.N_num))

        self.last_node = None
        self.cur_node = self.cur_path[self.i]

        self.last_node = None

    def traverse(self):
        while len(self.visited_cities) < self.N_num:
            self.visited_cities.add(self.cur_node)

            self.last_node = self.cur_node
            self.cur_node = self.cur_path[self.i % self.N_num]

            self.update_traversal(self.last_node, self.cur_node)
            self.i += 1
            yield

    def update_traversal(self, last_node, cur_node):
        if last_node is not None:
            self.edge_connections[last_node, cur_node] = 1
            self.edge_connections[cur_node, last_node] = 1

            self.edge_colors[last_node, cur_node] = colors["BRIGHT_WHITE"]
            self.edge_colors[cur_node, last_node] = colors["BRIGHT_WHITE"]

            self.N_colors[last_node] = colors["RED"]
