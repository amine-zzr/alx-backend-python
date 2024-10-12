#!/usr/bin/env python3
"""
This module provides a function to convert a string and a number into a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): An integer or floating-point number.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k
                           and the second element is the square of v.
    """
    return (k, float(v ** 2))
