# /usr/bin/env python3


import pygame as pg
import time
import numpy as np

from .constants import (
    E_COLOR,
    SCR_SIZE,
    BG_COLOR,
    RED,
    NODE_RADIUS,
    SEARCH_RATE,
    SEARCH_METHOD,
    NUM_NODES,
    MODE_SEARCH,
    MODE_TSP
)


from .Graph import Graph


class Game:
    def __init__(self, mode: str) -> None:
        pg.init()

        # main attributes of the game
        self.graph = Graph(n=NUM_NODES)
        
        if mode == MODE_SEARCH:
            self.search = SEARCH_METHOD()
            self.search.graph = self.graph
            self.search_generator = self.search.search()

        elif mode == MODE_TSP:
            # raise NotImplementedError
            pass

        # pg initialization
        self.screen = pg.display.set_mode(SCR_SIZE)
        self.graph_surf = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        pg.display.set_caption(f"Search Method: {self.search.name}")

        # more helper attributes
        self.font = pg.font.Font(None, 36)
        self.bg_surf = pg.Surface(self.screen.get_size())
        self.bg_surf.fill(BG_COLOR)

        # control flow related attributes
        self.start_iterations = False
        self.running = True

        print("🐼 searchViz has been initialized! 🎉")

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                print("\n\t🐼 Bye from searchViz 🔥")
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    click_x, click_y = event.pos
                    pg.draw.circle(
                        self.graph_surf,
                        RED,
                        (click_x, click_y),
                        radius=5 * NODE_RADIUS,
                    )

            # Handle spacebar key press
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.start_iterations = not self.start_iterations

        return None

    def draw_graph(self) -> None:
        # _start_time = time.time()
        # print("\n🕰️\tDrawing the Graph")

        # Unpack frequently used variables
        graph_surf = self.graph_surf
        num_nodes = self.graph.N_num
        nodes = self.graph.N_locs
        colors = self.graph.N_colors
        radius = self.graph.N_radii
        edges = self.graph.edge_connections
        edge_colors = self.graph.edge_colors

        # Draw edges
        edge_indices = np.transpose(np.where(edges))
        for i, j in edge_indices:
            # TODO: tuple type conversion overhead? Probably not
            pg.draw.line(graph_surf, tuple(edge_colors[i, j]), tuple(nodes[i]), tuple(nodes[j]))

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

    def run(self) -> None:
        last_time = pg.time.get_ticks()
        step = 0
        self.draw_graph()

        while self.running:
            cur_time = pg.time.get_ticks()

            self.screen.blit(self.bg_surf, (0, 0))
            self.handle_events()
            self.screen.blit(self.graph_surf, (0, 0))

            _txt = self.font.render(f"searchViz: {step}", 1, (255, 255, 255))
            self.screen.blit(_txt, (10, 10))

            pg.display.flip()

            # Time control
            if self.start_iterations:
                _delta = cur_time - last_time
                if _delta >= SEARCH_RATE * 1000:
                    step += 1
                    last_time = cur_time
                    # APPLY SEARCH HERE
                    try:
                        next(self.search_generator)
                        self.graph_surf.blit(self.bg_surf, (0, 0))
                        self.draw_graph()

                    except StopIteration:
                        self.start_iterations = False

        pg.quit()
