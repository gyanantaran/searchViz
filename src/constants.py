#!/usr/bin/env python

from .models import nodes_dist_wrapper, edge_dist_wrapper


# Screen configuration
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BG_COLOR = (0, 0, 0)  # Background color (RGB)


# Search configuration
NUM_NODES = 1000
NODE_RADIUS = 2


# distribution of nodes, available options: uniform, gaussian
NODES_X_DISTRIBUTION = nodes_dist_wrapper(SCREEN_WIDTH, model="gaussian")
NODES_Y_DISTRIBUTION = nodes_dist_wrapper(SCREEN_HEIGHT, model="gaussian")


# available options threshold, exponential
MAX_EDGE_LEN = 30
MIN_EDGE_LEN = 17
EDGE_CONFIDENCE = edge_dist_wrapper(
    max_edge_len=MAX_EDGE_LEN, min_edge_len=MIN_EDGE_LEN, model="exponential"
)


# Colours
RED = (255, 0, 0, 50)
BLUE = "cyan"
WHITE = (255, 255, 255, 200)
