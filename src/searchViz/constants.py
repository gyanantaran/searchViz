#!/usr/bin/env python

from .models import nodes_dist_wrapper, edge_dist_wrapper


# Screen configuration
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 850
SCR_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BG_COLOR = (0, 0, 0)  # Background color (RGB)


# Search configuration
NUM_NODES = 5000
NODE_RADIUS = 2

SEARCH_RATE = 0.5

# MODEL CONFIGURATIONS
# distribution of nodes, available options: uniform, gaussian
NODE_X_MODEL = "uniform"
NODE_Y_MODEL = "uniform"

# available options threshold, exponential
EDGE_MODEL = "threshold"
MAX_EDGE_LEN = 20
MIN_EDGE_LEN = 15


# OTHERS
NODES_X_DISTRIBUTION = nodes_dist_wrapper(SCREEN_WIDTH, model=NODE_X_MODEL)
NODES_Y_DISTRIBUTION = nodes_dist_wrapper(SCREEN_HEIGHT, model=NODE_Y_MODEL)

EDGE_CONFIDENCE = edge_dist_wrapper(
    max_edge_len=MAX_EDGE_LEN, min_edge_len=MIN_EDGE_LEN, model=EDGE_MODEL
)

# Colours (R G B A), A is the opacity (255 is opaque)
RED = (255, 0, 0, 255)
BLUE = (0, 255, 255, 255)
WHITE = (255, 255, 255, 200)
