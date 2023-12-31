#!/usr/bin/env python

from .search_utils import ReconstructPath, MakePairs, RemoveSeen

from ..constants import E_THICKNESS, NUM_NODES, SCR_SIZE

from ..graphViz.Graph import Graph

from .._typing import NodeCount, NodeType, NodeList

from numpy import mean, random, where, transpose, zeros, array
import pygame as pg


class Search(Graph):
    def __init__(self, n: NodeCount | int, name: str):
        super().__init__(n)

        self.name = name

        # Search stuff

        # start and end nodes
        start, goal = random.randint(0, self.N_num, size=2, dtype=NodeCount)
        self.start = start
        self.goal = goal

        self.N_colors[start] = self.colors["YELLOW"]
        self.N_colors[goal] = self.colors["RED"]

        # HARDCODED the ratio to NODE_RADIUS
        self.N_radii[start] = 3 * self.NODE_RADIUS
        self.N_radii[goal] = 3 * self.NODE_RADIUS

        self.open_ids, self.closed_ids = [], []

        self.origin = array(SCR_SIZE) / 2
        self.shift_effect = 0
        self.shifted_locs = zeros((self.N_num, 2))

        self.avg_window = 20
        self.shifted_effects = zeros((self.avg_window, 2))

    def draw_graph(self, graph_surf) -> None:
        # TODO: need make faster, blitting only those nodes/edges
        # that were updated

        # _start_time = time.time()
        # print("\n🕰️\tDrawing the Graph")

        if len(self.open_ids) > 0:
            effect = self.shift_effect * (
                self.N_locs[self.open_ids[0], :] - self.origin
            )
            self.shifted_effects[:-1, :] = self.shifted_effects[1:, :]
            self.shifted_effects[-1, :] = effect

            self.shifted_locs = self.N_locs

        N_locs = self.N_locs - mean(self.shifted_effects, axis=0)

        # Draw edges
        edge_indices = transpose(where(self.edge_connections))
        edge_colors = self.edge_colors[edge_indices[:, 0], edge_indices[:, 1]]

        for (i, j), color in zip(edge_indices, edge_colors):
            pg.draw.line(
                graph_surf,
                tuple(color),
                tuple(N_locs[i]),
                tuple(N_locs[j]),
                E_THICKNESS,
            )

        # Draw nodes
        N_colors = self.N_colors.astype(int)
        N_radii = self.N_radii.astype(int)
        node_data = list(
            zip(
                N_colors,
                N_locs.astype(int),
                N_radii,
            )
        )
        for color, loc, radius in node_data:
            pg.draw.circle(graph_surf, tuple(color), tuple(loc), radius)

            # _txt = self.font.render(f"{i}", 1, (255, 255, 255))
            # graph_surf.blit(_txt, nodes[i])

        # _end_time = time.time()
        # _elapsed_time = _end_time - _start_time
        # print("✅\tCompleted the drawing!\n")

        # print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

        return None

    ########################################################################
    #                   THE MOVEGEN AND GOALTEST FUNCTIONS
    ########################################################################

    def MoveGen(self, state: NodeType) -> NodeList:
        """
        Takes a state and returns an array of neighbors
        """
        neighbors = []

        node_id = 0
        while node_id < self.N_num:
            if (
                self.edge_connections[node_id, state]
                or self.edge_connections[state, node_id]
            ):
                neighbors.append(node_id)

            node_id += 1

        return neighbors

    def GoalTest(self, state: NodeType) -> bool:
        foundGoal = state == self.goal

        return foundGoal

    def update_traversal(self, closedNodePair, newNodesToOpen):
        closed_id = closedNodePair[0]
        open_ids = []
        open_parent_ids = set()
        for node in newNodesToOpen:
            open_ids.append(node[0])
            open_parent_ids.add(node[1])

        self.open_ids[0:1] = open_ids
        self.closed_ids.insert(0, closed_id)

        # NOTE: HARDCODED the ratio to NODE_RADIUS
        self.N_colors[open_ids] = self.colors["BLUE"]
        self.N_radii[open_ids] = 1.25 * self.NODE_RADIUS

        self.N_colors[closed_id] = self.colors["RED"]
        self.N_radii[closed_id] = 1.5 * self.NODE_RADIUS

        # Update edge-colors
        for parent in open_parent_ids:
            for child_id in open_ids:
                # Note: HARDCODED the increase in opacity of traversed edges
                self.edge_colors[parent, child_id][3] += 200
                self.edge_colors[child_id, parent][3] += 200

        return

    def search(self):
        raise NotImplementedError


class depthfirstsearch(Search):
    def __init__(self, n: NodeCount | int = NUM_NODES):
        name = "DFS"
        super().__init__(n, name)

    def search(self):
        open = [(self.start, None)]
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.GoalTest(node):
                print("Found goal!")
                path = [node for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed.insert(0, nodePair)

                # time-hogs because of stack creations because of function call
                children = self.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)

                open[0:1] = new

                self.update_traversal(nodePair, new)

                yield
        print("No path found")
        return -1


class breadthfirstsearch(Search):
    def __init__(self, n: NodeCount | int = NUM_NODES):
        name = "DFS"
        super().__init__(n, name)

    def search(self):
        open = [(self.start, None)]
        closed = []

        while len(open) > 0:
            nodePair = open[0]
            node = nodePair[0]
            if self.GoalTest(node):
                print("Found goal!")
                path = [node for node in ReconstructPath(nodePair, closed)]
                print(path)
                return path
            else:
                closed.insert(0, nodePair)

                # time-hogs because of stack creations because of function call
                children = self.MoveGen(node)
                noLoops = RemoveSeen(children, open, closed)
                new = MakePairs(noLoops, node)

                open[0:] = open[1:] + new

                self.update_traversal(nodePair, new)

                yield
        print("No path found")
        return -1
