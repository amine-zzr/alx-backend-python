#!/usr/bin/env python3
"""
This module provides a function to calc the sum of list of integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers and returns the result.

    Args:
        mxd_lst (List[Union[int, float]]): list of integers and/or float.

    Returns:
        float: The sum of all numbers in the list.
    """
    return float(sum(mxd_lst))
