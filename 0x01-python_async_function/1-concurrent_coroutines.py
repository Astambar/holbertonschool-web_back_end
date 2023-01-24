#!/usr/bin/env python3
""" 1-concurrent_coroutines.py """
import asyncio
import importlib
from typing import List

wait_random = importlib.import_module("0_basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
	"""_summary_

	Args:
		n (int): _description_
		max_delay (int): _description_

	Returns:
		List[float]: _description_
	"""
	tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
	delays = [await task for task in asyncio.as_completed(tasks)]
	return sorted(delays)
