#!/usr/bin/env python3
""" 0-simple_helper_function.py """


def index_range(page, page_size) -> tuple:
    """ index_range function """
    return ((page - 1) * page_size, page * page_size)
