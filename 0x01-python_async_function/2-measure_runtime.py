#!/usr/bin/env python3
""" 2-measure_runtime """
import time
from typing import Tuple

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    start_time = time.time()
    total_time = time.time() - start_time
    return total_time / n
