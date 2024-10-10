#!/usr/bin/env python3

"""
   101-safely_get_value
"""

from typing import Mapping, Any, Union, TypeVar

r = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[r, None] = None) -> Union[Any, r]:
    if key in dct:
        return dct[key]
    else:
        return default
