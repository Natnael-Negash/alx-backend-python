#!/usr/bin/env python3
"""Contains a function to measure the execution time of wait_n."""
import asyncio
import time
from typing import Tuple

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: Average time per call in seconds.
    """

    start_time = time.time()
    result = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_call = total_time / n

    return average_time_per_call
