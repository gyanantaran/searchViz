#!/usr/bin/env python3

from searchViz.Game import Game


def main():
    mode = "search"
    aGame = Game(mode=mode)
    aGame.run()


if __name__ == "__main__":
    main()
