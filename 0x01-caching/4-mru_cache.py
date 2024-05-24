#!/usr/bin/env python3
"""
Task 2: LIFO caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """i
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                first_key = self.cache_data.popitem(True)[0]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in
        self.cache_data linked to key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)
