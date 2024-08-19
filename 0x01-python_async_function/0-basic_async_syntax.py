#!/usr/bin/env python3
"""
module containing a courtine that introduces a 
rondom delay and returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns the delay.


    Args:

        max_delay(int): The maximum number of second to wait (inclusive).
                        The delay is a random float between 0 and max_delay.
                        Defaults to 10 seconds.


    Returns:
        
        float: Teh actual delay time in seconds that the coroutine waited.


    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay



