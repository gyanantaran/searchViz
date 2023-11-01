# utils to create node locations and edge connections

from threading import Event, Thread
from time import sleep

from numpy import column_stack, random, triu_indices, zeros

from .._typing import NodeCount, NodeCount, NodeLocs
from ..constants import EDGE_CONFIDENCE, N_X_DISTRIBUTION, N_Y_DISTRIBUTION


def create_node_locs(n: NodeCount) -> NodeLocs:
    """
    Returns a vector of `n` points, colors, radii:
    [
      (5.0, 0.1)
      (2.1, 5.0)
          ...
      (3.1, 4.0)
    ]
    according to a distribution function defined in constants
    """

    print(f"🕰️\tCreating {n} nodes... timer started...")
    x_values = N_X_DISTRIBUTION(int(n))
    y_values = N_Y_DISTRIBUTION(int(n))

    node_locs = column_stack((x_values, y_values))

    print("✅\tFinished creating nodes!\n")

    return node_locs


def create_edges(nodes: NodeLocs):
    """
    Creates edges for the give nodes locations
    """
    # TODO: need to seperate the threading or remove the animation
    global done
    done = Event()

    dot_thread = Thread(target=animate_dots)
    dot_thread.start()

    n = len(nodes)
    edge_connections = zeros((n, n))
    i, j = triu_indices(n, k=1)  # only one way edges

    _toss = random.rand(n, n)
    _confidence = zeros((n, n))
    _confidence[i, j] = EDGE_CONFIDENCE(nodes[i], nodes[j])

    # confidence number of times there will be an edge
    edge_connections = _toss <= _confidence

    # Stop the dot animation
    done.set()
    dot_thread.join()  # Wait for the animation thread to finish

    print("\n✅\tFinished creating edges!\n")
    return edge_connections


# for animating while the edges get created
def animate_dots():
    symbols = [".", "..", "...", "...🐌"]
    while not done.is_set():
        for symbol in symbols:
            print(f"🕰️\tCreating edges {symbol}", end=" \r", flush=True)
            sleep(0.25)
    return
