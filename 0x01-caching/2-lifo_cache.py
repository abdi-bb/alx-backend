#!/usr/bin/env python3
'''
Module: '2-lifo_cache'
Class: LIFOCache that inherits from BaseCaching
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    Caching system that manages cache based on LIFO order
    '''

    def __init__(self):
        '''Overloads the parent instantiation'''
        super().__init__()
        self.key_stack = []

    def put(self, key, item):
        '''
        Ties the item with the key in the parent's cache_data dict
        '''
        if key and item:
            self.cache_data[key] = item
            self.key_stack.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.key_stack.pop(-2)
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')

    def get(self, key):
        '''
        Returns the value tied to the key, if it exists
        '''
        return self.cache_data.get(key)
