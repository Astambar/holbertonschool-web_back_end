#!/usr/bin/env python3
""" 2-measure_runtime """
import time
from typing import Tuple

wait_n = __import__("1-concurrent_coroutines").wait_n

def measure_time(n: int, max_delay: int) -> float:
	""" measure_time """
	start_time = time.time()
	result = wait_n(n, max_delay)
	total_time = time.time() - start_time
	return total_time / n

n = 5
max_delay = 9

print(measure_time(n, max_delay))