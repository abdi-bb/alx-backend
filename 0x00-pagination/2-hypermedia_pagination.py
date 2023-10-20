#!/usr/bin/env python3
'''
Module: '2-hypermedia_pagination'
'''

import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''Returns tuple of start index and end index'''
    return ((page - 1) * page_size, page * page_size)


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
        """Retrieve a specific page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.start_index, self.end_index = index_range(page, page_size)
        dataset = self.dataset()
        if self.start_index >= len(dataset) or self.end_index > len(dataset):
            return []
        return dataset[self.start_index:self.end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        '''
        Returns a dictionary of pagination related params
        '''
        dataset = self.dataset()
        returned_dataset = self.get_page(page, page_size)

        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1

        if self.end_index < len(dataset):
            next_page = page + 1
        else:
            next_page = None

        total_pages = math.ceil(len(dataset) / page_size)
        return {
            'page_size': len(returned_dataset),
            'page': page,
            'data': returned_dataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
