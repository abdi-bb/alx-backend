#!/usr/bin/env python3
'''
Module: '0-simple_helper_function'
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''Returns tuple of start index and end index'''
    return ((page - 1) * page_size, page * page_size)
