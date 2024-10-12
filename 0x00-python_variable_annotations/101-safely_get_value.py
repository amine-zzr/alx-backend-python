#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""

from typing import Mapping, Any, Optional, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any, default: Optional[T] = None
) -> Optional[T]:
    """
    Safely retrieves the value from a dictionary for a given key.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key whose value is to be retrieved.
        default (Optional[T]): The default value if the key is not found.

    Returns:
        Optional[T]: value corresponding to the key,otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
