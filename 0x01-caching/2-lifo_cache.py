#!/usr/bin/env python3
"""
Task 2: LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                first_key = self.cache_data.popitem()[0]
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in
        self.cache_data linked to key
        """
        if key is None:
            return None
        else:
            return self.cache_data.get(key, None)
