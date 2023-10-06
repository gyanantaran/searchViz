# /usr/bin/env python3


import pygame
import time

from .constants import SCREEN_SIZE, BG_COLOR, RED, WHITE, NODE_RADIUS, BLUE

from .Search import Search
from .Graph import nodes, edges


class Game:
    def __init__(self, search_method: Search, num_nodes: int):
        # search method
        self.search_method = search_method
        self.num_nodes = num_nodes

        _start_time = time.time()
        print("creating nodes... timer started...")
        self.nodes = nodes(num_nodes)
        print("Finished creating nodes!")
        print("creating edges...")
        self.edges = edges(self.nodes)
        _end_time = time.time()
        _elapsed_time = _end_time - _start_time
        print(f"Finished creating edges! Took {_elapsed_time:.3f} seconds.")

        # pygame initialization
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(f"Search Method: {search_method.name}")

    def run(self):
        n = self.num_nodes
        nodes = self.nodes
        screen = self.screen

        # Precompute some values outside the loop
        bg_surface = pygame.Surface(screen.get_size())
        bg_surface.fill(BG_COLOR)

        graph_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        # Draw nodes and their edges
        for i in range(n):
            # Unique (uni-directional) edges
            for j in range(i, n):
                if self.edges[i, j]:
                    pygame.draw.line(graph_surface, WHITE, nodes[i], nodes[j])

            node = nodes[i]
            pygame.draw.circle(graph_surface, BLUE, node, radius=NODE_RADIUS)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        click_x, click_y = event.pos

                        pygame.draw.circle(
                            graph_surface,
                            RED,
                            (click_x, click_y),
                            radius=5 * NODE_RADIUS,
                        )

            # Clear the screen once at the beginning of the frame
            screen.blit(bg_surface, (0, 0))
            screen.blit(graph_surface, (0, 0))

            # Update game logic here

            pygame.display.flip()

        pygame.quit()
