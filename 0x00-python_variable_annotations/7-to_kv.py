#!/usr/bin/env python3

"""
   7-to_kv
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    r = float(v ** 2)
    return (k, r)
