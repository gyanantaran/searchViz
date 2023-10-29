#!/usr/bin/env python3

from searchViz.Game import Game
from searchViz.constants import NUM_NODES, SEARCH_METHOD


def main():
    search = SEARCH_METHOD()
    aGame = Game(search=search, num_nodes=NUM_NODES)

    aGame.run()


if __name__ == "__main__":
    main()
