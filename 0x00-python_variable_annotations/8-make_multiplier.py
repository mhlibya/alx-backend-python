#!/usr/bin/env python3
"""
   8-make_multiplier
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
       returns a function that multiplies two floats
    """
    def func(n: float):
        """
           mulfiplies two floats
        """
        return n * multiplier
    return func
