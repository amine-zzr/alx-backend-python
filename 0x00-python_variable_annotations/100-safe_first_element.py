#!/usr/bin/env python3
"""
This module provides a function to safely return the 1st element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence (like a list or a tuple) of any type.

    Returns:
        Union[Any, None]: The first element of the sequence, or None.
    """
    if lst:
        return lst[0]
    else:
        return None
