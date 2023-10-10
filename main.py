#!/usr/bin/env python3

from src.searchViz.Game import Game
from src.searchViz.Search import dfs

from src.searchViz.constants import NUM_NODES


def main():
    aGame = Game(search_method=dfs, num_nodes=NUM_NODES)
    aGame.run()


if __name__ == "__main__":
    main()
