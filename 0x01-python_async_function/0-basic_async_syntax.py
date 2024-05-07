#!/usr/bin/env python3

"""
an asynchronous coroutine function
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    an asynchronous coroutine that takes in an integer argument, wait_random,
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and returns it.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
