# utility function used in `Search.py`


def RemoveSeen(nodeList, openList, closedList):
    """A recursive function to remove seen nodes from nodeList"""
    if nodeList == []:
        return []
    else:
        n = nodeList[0]
        if OccursIn(n, openList) or OccursIn(n, closedList):
            return RemoveSeen(nodeList[1:], openList, closedList)
        else:
            return [n] + RemoveSeen(nodeList[1:], openList, closedList)


def OccursIn(node, listOfPairs):
    """Returns true if node[0] in the pairs[0] inside listOfPairs"""
    if listOfPairs == []:
        return False
    else:
        if node == listOfPairs[0][0]:
            # print(f"The node {node} \n\n {listOfPairs}\n")
            return True
        else:
            # print(f"for node {node} \n\n is not in {listOfPairs}\n")
            return OccursIn(node, listOfPairs[1:])


def MakePairs(list, parent):
    if list == []:
        return []
    else:
        return [(list[0], parent)] + MakePairs(list[1:], parent)


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
    if child == closed[0][0]:
        return closed[0]
    else:
        return FindLink(child, closed[1:])
