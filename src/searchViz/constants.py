#!/usr/bin/env python

from .graphViz.models import N_Distbn, E_Distbn

# Mode configuration
SEARCH_MODE = "search"
TSP_MODE = "tsp"


# TSP configuration
ACO_MODE = "ACO"
RANDOM_MODE = "Random"
GREEDY_MODE = "Greedy"
TSP_METHOD = RANDOM_MODE

# SEARCH CONFIGURATION
# available options: dfs, bfs
SEARCH_METHOD = "bfs"

GAME_MODE = SEARCH_MODE
ITERATION_RATE = 10


# Graph configuration
NUM_NODES = 3000
NODE_RADIUS = 1
E_THICKNESS = 1


# Colours (R G B A), A is the opacity (255 is opaque)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 255, 255, 255)
BRIGHT_WHITE = (255, 255, 255, 255)
WHITE = (255, 255, 255, 55)
YELLOW = (255, 255, 153, 200)
BLACK = (0, 0, 0, 255)
GREY = (125, 125, 150, 255)

BG_COLOR = BLACK  # Background color (RGB)
E_COLOR = WHITE

colors: dict = {
    "RED": RED,
    "GREEN": GREEN,
    "BLUE": BLUE,
    "WHITE": WHITE,
    "BRIGHT_WHITE": BRIGHT_WHITE,
    "YELLOW": YELLOW,
    "BLACK": BLACK,
    "GREY": GREY,
    "BG_COLOR": BG_COLOR,
}

NODE_COLOR = colors["GREY"]

# Screen configuration
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
SCR_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# MODEL CONFIGURATIONS
# distribution of nodes, available options: uniform, gaussian
NODE_X_MODEL = "gaussian"
NODE_Y_MODEL = "gaussian"

# available options threshold, exponential
E_MODEL = "threshold"
E_MAX_LEN = 20
E_MIN_LEN = 13

# OTHERS
N_X_DISTRIBUTION = N_Distbn(SCREEN_WIDTH, model=NODE_X_MODEL)
N_Y_DISTRIBUTION = N_Distbn(SCREEN_HEIGHT, model=NODE_Y_MODEL)

EDGE_CONFIDENCE = E_Distbn(max_len=E_MAX_LEN, min_len=E_MIN_LEN, model=E_MODEL)
