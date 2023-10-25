#!/usr/bin/env python3
'''
Module: '100-lfu_cache'
Class: 'LFUCache' that inherits from BaseCaching
'''

from base_caching import BaseCaching
from collections import Counter


class LFUCache(BaseCaching):
    '''
    Class LFUCache that manages cache based on lfu
    '''

    def __init__(self):
        '''Overloading the parent constructor'''
        super().__init__()
        self.key_frequency = []

    def put(self, key, item):
        '''
        Ties the item with the key in the parent's cache_data dict
        '''
        if key and item:
            self.cache_data[key] = item
            self.key_frequency.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                counter = Counter(self.key_frequency)
                min_frequency = min(counter.values())

                lfu_keys = [element for element, frequency in counter.items(
                ) if frequency == min_frequency]
                if len(lfu_keys) > 1:
                    # If there's more than one LFU key, use LRU
                    lru_key = self.key_frequency.pop(0)
                    # self.key_frequency.remove(lru_key)
                    del self.cache_data[lru_key]
                    print(f'DISCARD: {lru_key}')
                else:
                    lfu_key = lfu_keys[0]
                    self.key_frequency.remove(lfu_key)
                    del self.cache_data[lfu_key]
                    print(f'DISCARD: {lfu_key}')

    def get(self, key):
        '''
        Returns the value tied to the key, if it exists
        '''
        self.key_frequency.append(key)
        return self.cache_data.get(key)
