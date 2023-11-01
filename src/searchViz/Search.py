#!/usr/bin/env python

from .search_utils import ReconstructPath, MakePairs, RemoveSeen

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Graph import Graph


class Search(ABC):
    def __init__(self, name: str, graph): # TODO: type-hint graph argument to Search::__init__
        self.name = name
        # self.search = types.MethodType(search, Search)
        self.graph: Graph = graph

    @abstractmethod
    def search(self):
        raise NotImplementedError


class depthfirstsearch(Search):
    def __init__(self):
        self.name = "DFS"
        self.graph : Graph

        self.i = 0

    def search(self):
        open = [(self.graph.start, None)]
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.graph.GoalTest(node):
                print("Found goal!")
                path = [node for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed.insert(0, nodePair)

                # the following methods are time-hogs because of stack creations because of function calls
                children = self.graph.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)

                open[0:1] = new

                self.graph.update_traversal(nodePair, new)

                yield
        print("No path found")
        return -1


class breadthfirstsearch(Search):
    def __init__(self):
        self.name = "BFS"
        self.graph: Graph

        self.i = 0

    def search(self):
        open = [(self.graph.start, None)]
        closed = []

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
