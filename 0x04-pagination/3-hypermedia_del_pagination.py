#!/usr/bin/env python3
import csv
from typing import List, Dict
"""_summary_

Returns:
    _type_: _description_
"""


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
        indexed_dataset = self.indexed_dataset()
        nb_items = len(indexed_dataset)
        assert 0 <= index < nb_items, f"Index out of range: {index}/{nb_items}"
        if index is None:
            index = 0

        start = index
        end = min(index + page_size, nb_items)

        while True:
            data = [indexed_dataset[i] for i in range(start, end)]
            if data:
                break
            start += 1
            end = min(end + page_size, nb_items)

        next_index = end
        return {'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': next_index}
