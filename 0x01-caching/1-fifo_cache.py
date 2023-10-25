#!/usr/bin/env python3
'''
Module: '1-fifo_cache'
Class: 'FIFOCache' and inherits from BaseCaching
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Class FIFOCache that manges cache based on FIFO
    '''

    def __init__(self):
        '''Overloading the parent class instantiation'''
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        '''
        Assigns item to the key inside cache_data dict
        '''
        if key and item:
            self.cache_data[key] = item
            self.key_queue.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.key_queue.pop(0)
            self.cache_data.pop(oldest_key)
            print(f'DISCARD: {oldest_key}')

    def get(self, key):
        '''
        Returns a value linked to the key
        '''
        return self.cache_data.get(key)
