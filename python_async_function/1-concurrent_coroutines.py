#!/usr/bin/env python3
""" 1-concurrent_coroutines.py """
import asyncio
from typing import List

# Importer la fonction wait_random du module 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ 
    Exécute la fonction wait_random n fois avec un délai maximum de max_delay.
    Retourne une liste des temps d'attente pour chaque exécution de wait_random.
    """
    list = []
    for i in range(n):
        # Ajouter le résultat de wait_random à la liste
        list.append(wait_random(max_delay))
    # Retourner la liste des temps d'attente dans l'ordre d'achèvement
    return [await i for i in asyncio.as_completed(list)]
