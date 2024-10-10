#!/usr/bin/env python3

"""
   9-element_length
"""

from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """
       returns tuples that contains the content and it's length
    """
    return [(i, len(i)) for i in lst]
