#!/usr/bin/env python3

from .Node import Node

import numpy as np

import typing
from numpy.typing import NDArray

# TODO: put Node.py Node class inside Graph file? Circular imports?
# from __future__ import annotations
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     pass


NodeType = Node
NodeLocs = NDArray[np.float64]
NodeList = typing.List[Node]
NodeCount = np.uint16
SearchMethod = typing.Callable[[], typing.List[Node]]
