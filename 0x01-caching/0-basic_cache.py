#!/usr/bin/env python3
'''
Module: '0-basic_cache'
class BasicCache that inherits from BaseCaching
'''

from base_caching import BaseCaching
# BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Caching system that inherits from BaseCaching class
    '''

    def put(self, key, item):
        '''
        Assigns the item for the key in the dict self.cache_data
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Returns the item linked to a key from self.cahe_data
        '''
        return self.cache_data.get(key)
