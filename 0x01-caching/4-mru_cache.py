#!/usr/bin/env python3
'''
Module: '4-mru_cache'
Class: 'MRUCache' that inherits from BaseCaching
'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    Class MRUCache that manages cache based on MRU
    '''

    def __init__(self):
        '''Overloading the parent constructor'''
        super().__init__()
        self.key_chronology = []

    def put(self, key, item):
        '''
        Ties the item with the key in the parent's cache_data dict
        '''
        if key and item:
            self.cache_data[key] = item
            if key not in self.key_chronology:
                self.key_chronology.append(key)
            else:
                self.key_chronology.append(
                    self.key_chronology.pop(self.key_chronology.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.key_chronology.pop(-2)
                del self.cache_data[lru_key]
                print(f'DISCARD: {lru_key}')

    def get(self, key):
        '''
        Returns the value tied to the key, if it exists
        '''
        if key in self.cache_data:
            self.key_chronology.append(
                self.key_chronology.pop(self.key_chronology.index(key)))
        return self.cache_data.get(key)
