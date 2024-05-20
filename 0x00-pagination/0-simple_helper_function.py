#!/usr/bin/env python3
"""
Task 0: Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:

    """
    takes two integer arguments page and page_size
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    return (((page_size * page) - page_size), (page * page_size))
