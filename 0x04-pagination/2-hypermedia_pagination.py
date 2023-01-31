#!/usr/bin/env python3
import math
"""_summary_

Returns:
    _type_: _description_
"""


class Server:
    def __init__(self):
        self.data = []
        with open("baby-names.csv", "r") as f:
            for line in f:
                self.data.append(line.split(","))

    def get_page(self, page, page_size):
        start = (page - 1) * page_size
        end = start + page_size
        return self.data[start:end]

    def get_hyper(self, page=1, page_size=10):
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.data) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
