#!/usr/bin/env python3
"""
Zooms into a list by repeating each element `factor` times.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into a list by repeating each element `factor` times.

    Args:
        lst (Sequence): The list or sequence of elements to zoom into.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List: A list where each element is repeated `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
