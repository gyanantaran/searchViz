#!/usr/bin/env python


class Search:
    def __init__(self, name, search_method):
        self.name = name
        self.search = search_method

    def search(self):
        # returns a method for searching
        print("Search Method was not defined")
        raise NotImplementedError


def depth_first_search():
    print("Depth First Search")


def breadth_first_search():
    print("Breadth First Search")


dfs = Search("Depth-first search", depth_first_search)
bfs = Search("Breadth-first search", breadth_first_search)


if __name__ == "__main__":
    dfs.search()
