#!/usr/bin/env python3

import random
import asyncio

async def wait_random(max_delay: int =10):
    x = random.uniform(0, max_delay)
    if not isinstance (max_delay, int):
        raise TypeError("Parameter 'max_delay' must be an integer.")
    await asyncio.sleep(x)
    return x
