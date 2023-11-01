#!/usr/bin/env python

import time

from numpy import full, transpose, uint8, where
import pygame as pg

from .._typing import NodeCount
from ..constants import NODE_COLOR, NODE_RADIUS, colors
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
        self.edge_colors = full((n, n, 4), fill_value=colors["WHITE"], dtype=uint8)

        # others
        self.font = pg.font.Font(None, 11)
        self.colors = colors
        self.NODE_COLOR = NODE_COLOR
        self.NODE_RADIUS = NODE_RADIUS

        _end_time = time.time()
        _elapsed_time = _end_time - _start_time

        print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

    # TODO: Need to make this faster by blitting only those nodes/edges that were updated
    def draw_graph(self, graph_surf) -> None:
        # _start_time = time.time()
        # print("\n🕰️\tDrawing the Graph")

        # Unpack frequently used variables
        num_nodes = self.N_num

        nodes = self.N_locs
        colors = self.N_colors
        radius = self.N_radii
        edges = self.edge_connections
        edge_colors = self.edge_colors

        # Draw edges
        edge_indices = transpose(where(edges))
        for i, j in edge_indices:
            # TODO: tuple type conversion overhead? Probably not
            pg.draw.line(
                graph_surf, tuple(edge_colors[i, j]), tuple(nodes[i]), tuple(nodes[j])
            )

        # Draw nodes
        # TODO: vectorization of this possible? Probably not
        for i in range(num_nodes):
            pg.draw.circle(
                graph_surf, color=colors[i], center=nodes[i], radius=radius[i]
            )

            # _txt = self.font.render(f"{i}", 1, (255, 255, 255))
            # graph_surf.blit(_txt, nodes[i])

        # _end_time = time.time()
        # _elapsed_time = _end_time - _start_time
        # print("✅\tCompleted the drawing!\n")

        # print(f"\t🕰️ Took {_elapsed_time:.3f} seconds.\n")

        return None
