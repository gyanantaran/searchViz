# utility function used in `Search.py`

from typing import List


def RemoveSeen(nodeList: List, openList: List, closedList: List):
    """An iterative function to remove seen nodes from nodeList"""
    seen_nodes = set()
    seen_nodes.update(pair[0] for pair in openList)
    seen_nodes.update(pair[0] for pair in closedList)

    result = [n for n in nodeList if n not in seen_nodes]
    return result


def OccursIn(node, listOfPairs):
    for pair in listOfPairs:
        if node == pair[0]:
            return True
    return False


def MakePairs(list, parent):
    pairs = []
    for item in list:
        pairs.append((item, parent))
    return pairs


def ReconstructPath(nodePair: tuple, closed: List):
    path = [nodePair[0]]
    parent = nodePair[1]

    while parent is not None:
        path = [parent] + path
        nodePair = FindLink(parent, closed)

        parent = nodePair[1]
    return path


def FindLink(child: int, closed: List) -> tuple:
    for link in closed:
        if child == link[0]:
            return link
    return ()
