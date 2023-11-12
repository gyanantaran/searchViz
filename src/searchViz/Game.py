# /usr/bin/env python3


import pygame as pg

from .constants import (
    SCR_SIZE,
    colors,
    GAME_MODE,
    ITERATION_RATE,
    TSP_MODE,
    TSP_METHOD,
    SEARCH_MODE,
    SEARCH_METHOD,
)
from .searchViz.Search import depthfirstsearch, breadthfirstsearch
from .tspViz.TSP import ACO, Random, Greedy


class Game:
    def __init__(self) -> None:
        pg.init()

        self.game_mode = GAME_MODE

        # main attributes of the game
        if self.game_mode == SEARCH_MODE:
            # need to figure out a better way to switch search method
            match SEARCH_METHOD:
                case "dfs":
                    search = depthfirstsearch()
                case "bfs":
                    search = breadthfirstsearch()
                case _:
                    search = depthfirstsearch()

            search_generator = search.search()

            self.mode = search
            self.mode_generator = search_generator

        elif self.game_mode == TSP_MODE:
            match TSP_METHOD:
                case "ACO":
                    tsp = ACO()
                case "Greedy":
                    tsp = Greedy()
                case "Random":
                    tsp = Random()
                case _:
                    exit(1)

            tsp_generator = tsp.traverse()

            self.mode = tsp
            self.mode_generator = tsp_generator

        self.mode_iter = 0

        # pg initialization
        self.screen = pg.display.set_mode(SCR_SIZE)
        self.graph_surf = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        pg.display.set_caption(f"{self.game_mode} Method: {self.mode.name}")

        # more helper attributes
        self.font = pg.font.Font(None, 36)
        self.bg_surf = pg.Surface(self.screen.get_size())
        self.bg_surf.fill(colors["BG_COLOR"])

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
                        self.screen,
                        colors["RED"],
                        (click_x, click_y),
                        radius=5,
                    )

            # Handle spacebar key press
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.start_iterations = not self.start_iterations

        return None

    def set_screen(self):
        self.screen.blit(self.bg_surf, (0, 0))
        self.handle_events()
        self.screen.blit(self.graph_surf, (0, 0))

        _txt = self.font.render(
            f"{self.game_mode}Viz: {self.mode_iter}", 1, (255, 255, 255)
        )
        self.screen.blit(_txt, (10, 10))

    def run(self) -> None:
        last_time = pg.time.get_ticks()
        self.mode.draw_graph(self.graph_surf)

        while self.running:
            cur_time = pg.time.get_ticks()
            self.set_screen()

            # Time control
            if self.start_iterations:
                _delta = cur_time - last_time
                if _delta >= ITERATION_RATE:
                    # APPLY GENERATOR HERE
                    try:
                        next(self.mode_generator)
                        self.graph_surf.blit(self.bg_surf, (0, 0))
                        self.mode.draw_graph(self.graph_surf)

                    except StopIteration:
                        self.start_iterations = False

                    self.mode_iter += 1
                    last_time = cur_time

            pg.display.flip()

        pg.quit()
