#!/usr/bin/env python3

import numpy as np

import typing
from numpy.typing import NDArray

# TODO: put Node.py Node class inside Graph file? Circular imports?
# from __future__ import annotations
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     pass


NodeType = np.uint16
NodeLocs = NDArray[np.float64]
NodeList = typing.List[NodeType]
NodeCount = np.uint16
SearchMethod = typing.Callable[[], NodeList]
