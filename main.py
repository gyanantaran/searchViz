#!/usr/bin/env python3

from src.Game import Game
from src.Search import dfs

from src.constants import NUM_NODES


def main():
    aGame = Game(search_method=dfs, num_nodes=NUM_NODES)

    aGame.run()


if __name__ == "__main__":
    main()
