#!/usr/bin/env python3

from searchViz.Game import Game
from searchViz.Search import depthfirstsearch
from searchViz.constants import NUM_NODES

from searchViz._typing import NodeCount

# to hide the message


def main():
    dfs = depthfirstsearch()

    aGame = Game(search=dfs, num_nodes=NodeCount(NUM_NODES))

    aGame.run()


if __name__ == "__main__":
    main()
