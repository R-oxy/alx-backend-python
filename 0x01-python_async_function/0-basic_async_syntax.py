#!/usr/bin/env python3
"""Async function basics"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes in an argument, waits for a random delay, returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
