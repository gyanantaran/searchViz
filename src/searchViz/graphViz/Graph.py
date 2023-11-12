#!/usr/bin/env python

import time

from numpy import full, transpose, uint8, where, arange
import pygame as pg

from .._typing import NodeCount
from ..constants import E_THICKNESS, NODE_COLOR, NODE_RADIUS, colors
from .graph_utils import create_edges, create_node_locs


class Graph:
    def __init__(self, n: NodeCount | int):
        _start_time = time.time()

        # Node stuff
        self.N_num = n
        self.N_colors = full((self.N_num, 4), NODE_COLOR, dtype=uint8)
        self.N_radii = full((self.N_num,), NODE_RADIUS, dtype=uint8)
        self.N_locs = create_node_locs(NodeCount(self.N_num))

        # Edge stuff
        self.edge_connections = create_edges(self.N_locs)
        self.edge_colors = full((n, n, 4), colors["WHITE"], uint8)

        # others
        self.font = pg.font.Font(None, 20)
        self.colors = colors
        self.NODE_COLOR = NODE_COLOR
        self.NODE_RADIUS = NODE_RADIUS

        _end_time = time.time()
        _elapsed_time = _end_time - _start_time

        print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

    def draw_graph(self, graph_surf) -> None:
        # TODO: need make faster, blitting only those nodes/edges
        # that were updated

        # _start_time = time.time()
        # print("\n🕰️\tDrawing the Graph")

        self.N_locs[:, 0] += 1

        # Draw edges
        edge_indices = transpose(where(self.edge_connections))
        edge_colors = self.edge_colors[edge_indices[:, 0], edge_indices[:, 1]]

        for (i, j), color in zip(edge_indices, edge_colors):
            pg.draw.line(
                graph_surf,
                tuple(color),
                tuple(self.N_locs[i]),
                tuple(self.N_locs[j]),
                E_THICKNESS,
            )

        # Draw nodes
        N_colors = self.N_colors.astype(int)
        N_radii = self.N_radii.astype(int)
        node_data = list(zip(N_colors, self.N_locs.astype(int), N_radii))
        for color, loc, radius in node_data:
            pg.draw.circle(graph_surf, tuple(color), tuple(loc), radius)

            # _txt = self.font.render(f"{i}", 1, (255, 255, 255))
            # graph_surf.blit(_txt, nodes[i])

        # _end_time = time.time()
        # _elapsed_time = _end_time - _start_time
        # print("✅\tCompleted the drawing!\n")

        # print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

        return None
