#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import random
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures total execution time for
    wait_n(n, max_delay)
    Returns:
        total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
