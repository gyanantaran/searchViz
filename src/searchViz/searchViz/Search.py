#!/usr/bin/env python

from .search_utils import ReconstructPath, MakePairs, RemoveSeen

# from typing import TYPE_CHECKING

from ..graphViz.Graph import Graph

from .._typing import NodeCount, NodeType, NodeList

from numpy import random


class Search(Graph):
    def __init__(self, n: NodeCount | int, name: str):
        super().__init__(n)

        self.name = name

        # Search stuff

        # start and end nodes
        start, goal = random.randint(0, self.N_num, size=2, dtype=NodeCount)
        self.start = start
        self.goal = goal

        self.N_colors[start] = self.colors["YELLOW"]
        self.N_colors[goal] = self.colors["RED"]

        # HARDCODED the ratio to NODE_RADIUS
        self.N_radii[start] = 3 * self.NODE_RADIUS
        self.N_radii[goal] = 3 * self.NODE_RADIUS

        self.open_ids, self.closed_ids = [], []

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
            if self.edge_connections[id, state] or self.edge_connections[state, id]:
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

        return foundGoal

    def update_traversal(self, closedNodePair, newNodesToOpen):
        closed_id = closedNodePair[0]
        open_ids = []
        open_parent_ids = set()
        for node in newNodesToOpen:
            open_ids.append(node[0])
            open_parent_ids.add(node[1])

        self.open_ids[0:1] = open_ids
        self.closed_ids.insert(0, closed_id)

        # NOTE: HARDCODED the ratio to NODE_RADIUS
        self.N_colors[open_ids] = self.colors["BLUE"]
        self.N_radii[open_ids] = 1.25 * self.NODE_RADIUS

        self.N_colors[closed_id] = self.colors["RED"]
        self.N_radii[closed_id] = 1.5 * self.NODE_RADIUS

        # Update edge-colors
        for parent in open_parent_ids:
            for child_id in open_ids:
                # Note: HARDCODED the increase in opacity of traversed edges
                self.edge_colors[parent, child_id][3] += 200
                self.edge_colors[child_id, parent][3] += 200

        return

    def search(self):
        raise NotImplementedError


class depthfirstsearch(Search):
    def __init__(self, n: NodeCount | int):
        name = "DFS"
        super().__init__(n, name)

    def search(self):
        open = [(self.start, None)]
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.GoalTest(node):
                print("Found goal!")
                path = [node for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed.insert(0, nodePair)

                # the following methods are time-hogs because of stack creations because of function calls
                children = self.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)

                open[0:1] = new

                self.update_traversal(nodePair, new)

                yield
        print("No path found")
        return -1


class breadthfirstsearch(Search):
    def __init__(self, n: NodeCount | int):
        name = "DFS"
        super().__init__(n, name)

    def search(self):
        open = [(self.start, None)]
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.GoalTest(node):
                print("Found goal!")
                path = [node for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed.insert(0, nodePair)

                # the following methods are time-hogs because of stack creations because of function calls
                children = self.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)

                open[0:] = open[1:] + new

                self.update_traversal(nodePair, new)

                yield
        print("No path found")
        return -1
