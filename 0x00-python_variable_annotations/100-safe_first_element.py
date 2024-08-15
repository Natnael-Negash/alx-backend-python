#!/usr/bin/env python3
"""Module containing code with correct duck-typed annotations."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a list or None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None
