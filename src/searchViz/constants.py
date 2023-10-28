#!/usr/bin/env python

from .models import N_Distbn, E_Distbn


# Screen configuration
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 850
SCR_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BG_COLOR = (0, 0, 0)  # Background color (RGB)


# Search configuration
NUM_NODES = 5000
NODE_RADIUS = 2

SEARCH_RATE = 0.0005

# MODEL CONFIGURATIONS
# distribution of nodes, available options: uniform, gaussian
NODE_X_MODEL = "uniform"
NODE_Y_MODEL = "uniform"

# available options threshold, exponential
E_MODEL = "threshold"
E_MAX_LEN = 20
E_MIN_LEN = 15

# OTHERS
NODES_X_DISTRIBUTION = N_Distbn(SCREEN_WIDTH, model=NODE_X_MODEL)
NODES_Y_DISTRIBUTION = N_Distbn(SCREEN_HEIGHT, model=NODE_Y_MODEL)

EDGE_CONFIDENCE = E_Distbn(max_len=E_MAX_LEN, min_len=E_MIN_LEN, model=E_MODEL)

# Colours (R G B A), A is the opacity (255 is opaque)
RED = (255, 0, 0, 255)
BLUE = (0, 255, 255, 255)
WHITE = (255, 255, 255, 255)
YELLOW = (255, 255, 153, 200)
