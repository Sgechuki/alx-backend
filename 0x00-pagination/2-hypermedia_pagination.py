#!/usr/bin/env python3
"""
Task 2: Hypermedia pagination
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

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        returns a dictionary containing
        the following key-value pairs
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        size: int = len(self.dataset())
        data: List[List] = self.get_page(page, page_size)
        if size % page_size == 0:
            total_pages: int = size // page_size
        else:
            total_pages: int = (size // page_size) + 1
        if page < total_pages:
            next_page: int = page + 1
        else:
            next_page: int = None
        if page > 1:
            prev_page: int = page - 1
        else:
            prev_page: int = None

        dct = {"page_size": len(data), "page": page,
               "data": data, "next_page": next_page,
               "prev_page": prev_page, "total_pages": total_pages}
        return dct
