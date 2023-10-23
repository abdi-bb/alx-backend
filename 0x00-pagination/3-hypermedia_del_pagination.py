#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    '''
    A deletion-resilient method that returns a dict of hypermedia dict
    '''
    indexed_dataset = self.indexed_dataset()
    dataset_length = len(indexed_dataset)

    # Verify that the requested index is within a valid range
    if index is not None and (index < 0 or index >= dataset_length):
        raise ValueError("Invalid index")

    if index is None:
        index = 0

    next_index = None
    page_data = []
    page_data_count = 0

    for idx in range(index, dataset_length):
        item = indexed_dataset.get(idx)
        if item is not None:
            page_data.append(item)
            page_data_count += 1
            if page_data_count == page_size:
                next_index = idx + 1
                break

    return {
        'index': index,
        'data': page_data,
        'page_size': page_size,
        'next_index': next_index,
    }
