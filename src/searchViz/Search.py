#!/usr/bin/env python

from .search_utils import ReconstructPath, MakePairs, RemoveSeen


def depthfirstsearch(self, start_state):
    open = [(start_state, None)]
    closed = []

    while len(open) > 0 and len(closed) < 50:
        print(f"open: {len(open)}")
        print(f"closed: {len(closed)}")
        nodePair = open[0]
        node = nodePair[0]
        # print(node)
        # print(f"closed {closed}")
        # print()
        if self.GoalTest(node) is True:
            print("Found goal!")
            return ReconstructPath(nodePair, closed)
        else:
            closed = [nodePair] + closed
            children = self.MoveGen(node)
            noLoops = RemoveSeen(children, open, closed)
            new = MakePairs(noLoops, node)
            open = new + open[1:]  # The only change from DFS
            yield open

    print("No path found")
    return -1
