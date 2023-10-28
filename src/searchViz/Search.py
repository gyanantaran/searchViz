#!/usr/bin/env python

from .search_utils import ReconstructPath, MakePairs, RemoveSeen
from .Graph import Graph


class Search:
    def __init__(self, name, graph: Graph):
        self.name = name
        # self.search = types.MethodType(search, Search)
        self.graph = graph

    def search(self):
        raise NotImplementedError


class depthfirstsearch(Search):
    def __init__(self):
        self.name = "DFS"
        self.graph: Graph

        self.i = 0

    def search(self):
        open = [(self.graph.start_node, None)]
        print(open[0][0].id)
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.graph.GoalTest(node) is True:
                # print("Found goal!")
                # print(path = ReconstructPath(nodePair, closed)])
                return
            else:
                closed = [nodePair] + closed
                children = self.graph.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)
                open = new + open[1:]  # The only change from DFS
                yield [nodepair[0].id for nodepair in open]

        # print("No path found")
        return -1
