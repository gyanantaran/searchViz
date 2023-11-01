#!/usr/bin/env python

from .models import N_Distbn, E_Distbn
from .Search import depthfirstsearch, breadthfirstsearch

# Mode configuration
MODE_SEARCH = "search"
MODE_TSP = "tsp"

# Screen configuration
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 950
SCR_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


# Search configuration
SEARCH_METHOD = depthfirstsearch
SEARCH_RATE = 0 #.0000000000000000005

# Graph configuration
NUM_NODES = 5000
NODE_RADIUS = 2


# MODEL CONFIGURATIONS
# distribution of nodes, available options: uniform, gaussian
NODE_X_MODEL = "uniform"
NODE_Y_MODEL = "uniform"

# available options threshold, exponential
E_MODEL = "threshold"
E_MAX_LEN = 24
E_MIN_LEN = 13

# OTHERS
N_X_DISTRIBUTION = N_Distbn(SCREEN_WIDTH, model=NODE_X_MODEL)
N_Y_DISTRIBUTION = N_Distbn(SCREEN_HEIGHT, model=NODE_Y_MODEL)

EDGE_CONFIDENCE = E_Distbn(max_len=E_MAX_LEN, min_len=E_MIN_LEN, model=E_MODEL)

# Colours (R G B A), A is the opacity (255 is opaque)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 255, 255, 255)
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
    "YELLOW": YELLOW,
    "BLACK": BLACK,
    "GREY": GREY,
}

NODE_COLOR = colors["GREY"]
