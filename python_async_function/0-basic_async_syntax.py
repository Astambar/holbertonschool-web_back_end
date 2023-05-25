#!/usr/bin/env python3
"""
Ce module contient la fonction wait_random qui attend
de manière asynchrone un délai aléatoire et le renvoie.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend de manière asynchrone un délai aléatoire
       entre 0 et max_delay (inclus) et le renvoie.

    Args:
        max_delay (int): Le délai maximum à attendre. Par défaut à 10.

    Returns:
        float: Le délai réel attendu.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
