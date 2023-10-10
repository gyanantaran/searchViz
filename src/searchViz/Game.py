# /usr/bin/env python3


import pygame
import numpy as np

from .constants import SCR_SIZE, BG_COLOR, RED, WHITE, NODE_RADIUS, SEARCH_RATE

from .Search import Search
from .Graph import Graph


class Game:
    def __init__(self, search_method: Search, num_nodes: int):
        pygame.init()

        # main attributes of the game
        self.search_method = search_method
        self.Graph = Graph(num_nodes)

        # pygame initialization
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(f"Search Method: {search_method.name}")

    def run(self):
        # unpacking frequently used variables
        num_nodes = self.Graph.num_nodes
        nodes = self.Graph.nodes
        colors = self.Graph.colors
        radius = self.Graph.radius
        edges = self.Graph.edges

        open = int(np.random.randint(0, num_nodes, 1)[0])
        closed = []

        screen = self.screen

        step = 1
        start_search = False
        font = pygame.font.Font(None, 36)
        last_step_update_time = pygame.time.get_ticks()

        # Precompute some values outside the loop
        bg_surface = pygame.Surface(screen.get_size())
        bg_surface.fill(BG_COLOR)

        graph_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        # Draw nodes and their edges
        for i in range(num_nodes):
            # Unique (uni-directional) edges
            for j in range(i, num_nodes):
                if edges[i, j]:
                    pygame.draw.line(graph_surface, WHITE, nodes[i], nodes[j])

            node = nodes[i]
            pygame.draw.circle(
                graph_surface,
                color=tuple(colors[i]),
                center=node,
                radius=radius[i],
            )

        running = True
        while running:
            current_time = pygame.time.get_ticks()
            # Clear the screen once at the beginning of the frame
            # graph_surface.blit(bg_surface, (0, 0))

            screen.blit(bg_surface, (0, 0))
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
                # Handle spacebar key press
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_search = not start_search

            screen.blit(graph_surface, (0, 0))

            # Update game logic here
            if start_search:
                # Calculate the time elapsed since the last step update
                time_elapsed = current_time - last_step_update_time

                # Check if 5 seconds (5000 milliseconds) have passed
                if time_elapsed >= SEARCH_RATE * 1000:
                    # Increment the step and update the last step update time
                    step += 1
                    last_step_update_time = current_time
                    # draw node

                    node = nodes[open]
                    pygame.draw.circle(
                        graph_surface,
                        color=RED,
                        center=nodes[open],
                        radius=2 * radius[open],
                    )

                    flag = False
                    for i in range(open, num_nodes):
                        connected = edges[open, i]
                        if connected:
                            closed.append(i)
                            open = i
                            flag = True
                            break

                    if not flag:
                        for i in range(0, open):
                            connected = edges[i, open]
                            if connected and (i not in closed):
                                closed.append(i)
                                open = i
                                flag = True
                                break
                    if not flag:
                        open = int(np.random.randint(0, num_nodes, 1)[0])

            step_text = font.render(f"Step: {step}", True, (255, 255, 255))
            screen.blit(step_text, (10, 10))  # Adjust the position as needed

            pygame.display.flip()

        pygame.quit()
