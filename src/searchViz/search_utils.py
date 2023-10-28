# utility function used in `Search.py`


def RemoveSeen(nodeList, openList, closedList):
    """An iterative function to remove seen nodes from nodeList"""
    result = []
    for n in nodeList:
        if not (OccursIn(n, openList) or OccursIn(n, closedList)):
            result.append(n)
    return result


def OccursIn(node, listOfPairs):
    for pair in listOfPairs:
        if node.id == pair[0].id:
            return True
    return False


def MakePairs(list, parent):
    pairs = []
    for item in list:
        pairs.append((item, parent))
    return pairs


def ReconstructPath(nodePair, closed):
    path = [nodePair[0]]
    parent = nodePair[1]

    while parent is not None:
        path = parent + path
        nodePair = FindLink(parent, closed)

        parent = nodePair[1]
    print(path)
    return path


def FindLink(child, closed):
    for link in closed:
        if child == link[0]:
            return link
    return []
