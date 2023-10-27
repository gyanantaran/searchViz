#!/usr/bin/env python

from typing import Callable, List

from .Graph import Node

import numpy as np


class Search:
    def __init__(self, search: Callable[[Node], List[Node]], name: str):
        self.search = search
        self.name = name


def depth_first_search(startState: Node) -> List[Node]:
    print("Depth First Search")
    return [startState]


def breadth_first_search(startState: Node) -> List[Node]:
    print("Breadth First Search")
    return [startState]


dfs = Search(depth_first_search, "Depth-first search")
bfs = Search(breadth_first_search, "Breadth-first search")


if __name__ == "__main__":
    startState = Node(np.uint16(1))
    dfs.search(startState)
