#!/usr/bin/env python3
""" 0-async_generator.py """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Générateur asynchrone qui renvoie 10
    nombres flottants aléatoires entre 0 et 10
    """
    for i in range(10):
        # Attendre 1 seconde avant de générer le prochain nombre aléatoire
        await asyncio.sleep(1)
        # Renvoyer un nombre flottant aléatoire entre 0 et 10
        yield random.uniform(0, 10)
