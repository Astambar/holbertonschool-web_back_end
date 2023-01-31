#!/usr/bin/env python3
"""_summary_
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start and end index of the range
    for the given pagination parameters.

    :param page: The current page number (1-indexed).
    :param page_size: The number of items per page.
    :return: A tuple of size two containing the start and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
