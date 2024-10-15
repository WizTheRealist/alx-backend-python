#!/usr/bin/env python3

import asyncio
import random
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    for _ in range(10):
        x = [random.random() * 10 async for _ in async_generator()]
        return x
