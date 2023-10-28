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
        closed = []

        print(open[0][0].id)

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.graph.GoalTest(node):
                print("Found goal!")
                path = [node.id for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed = [nodePair] + closed
                children = self.graph.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)
                open = new + open[1:]  # The only change from DFS

                self.graph.open_ids = open
                self.graph.closed_ids = closed

                yield
        print("No path found")
        return -1


class breadthfirstsearch(Search):
    def __init__(self):
        self.name = "BFS"
        self.graph: Graph

        self.i = 0

    def search(self):
        open = [(self.graph.start_node, None)]
        closed = []

        print(open[0][0].id)

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.graph.GoalTest(node):
                print("Found goal!")
                path = [node.id for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed = [nodePair] + closed
                children = self.graph.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)
                open = open[1:] + new  # The only change from DFS

                self.graph.open_ids = open
                self.graph.closed_ids = closed

                yield
        print("No path found")
        return -1
