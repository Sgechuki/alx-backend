#!/usr/bin/env python3
"""
Task 1: Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:

    """
    takes two integer arguments page and page_size
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    return (((page_size * page) - page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two integer arguments page with
        default value 1 and page_size with default value 10
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]
