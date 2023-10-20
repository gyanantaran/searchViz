#!/usr/bin/env python3

from searchViz.Game import Game
from searchViz.Search import dfs
from searchViz.constants import NUM_NODES

# to hide the message


def main():
    aGame = Game(search_method=dfs, num_nodes=NUM_NODES)

    aGame.run()


if __name__ == "__main__":
    main()
