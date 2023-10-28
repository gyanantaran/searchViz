import numpy as np


# Seperated from the Graph.py file because of circular imports in _typing.py
class Node:
    def __init__(self, id: np.uint16):
        """
        id: the id of the node, np.uint16 for maximum
            of 2^16 (= 65535 + 1) nodes on the screen
        """
        self.id = id
