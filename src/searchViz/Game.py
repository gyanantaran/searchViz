# /usr/bin/env python3


import pygame as pg
from .constants import SCR_SIZE, BG_COLOR, RED, WHITE, NODE_RADIUS, SEARCH_RATE


from .Search import Search
from .Graph import Graph


class Game:
    def __init__(self, search_method: Search, num_nodes: int):
        pg.init()

        # main attributes of the game
        self.search_method = search_method
        self.Graph = Graph(num_nodes)

        # pg initialization
        self.screen = pg.display.set_mode(SCR_SIZE)
        self.graph_surf = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        pg.display.set_caption(f"Search Method: {search_method.name}")

        # more helper attributes
        self.font = pg.font.Font(None, 36)
        self.bg_surf = pg.Surface(self.screen.get_size())
        self.bg_surf.fill(BG_COLOR)

        # control flow related attributes
        self.start_search = False
        self.running = True

        print("🐼 searchViz has been initialized! 🎉")

    def handle_events(self):
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
                    self.start_search = not self.start_search

        return None

    def draw_graph(self):
        # unpacking frequently used variables
        graph_surf = self.graph_surf
        num_nodes = self.Graph.num_nodes
        nodes = self.Graph.nodes
        colors = self.Graph.colors
        radius = self.Graph.radius
        edges = self.Graph.edges

        # need to use this when traversing
        # edge_colors = self.Graph.edge_color

        # Draw nodes and their edges
        for i in range(num_nodes):
            # Unique (uni-directional) edges
            for j in range(i, num_nodes):
                if edges[i, j]:
                    pg.draw.line(graph_surf, WHITE, nodes[i], nodes[j])

            node = nodes[i]
            pg.draw.circle(
                graph_surf,
                color=tuple(colors[i]),
                center=node,
                radius=radius[i],
            )

    def run(self):
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
            if self.start_search:
                _delta = cur_time - last_time
                if _delta >= SEARCH_RATE * 1000:
                    step += 1
                    last_time = cur_time
                    # APPLY SEARCH HERE

        pg.quit()
