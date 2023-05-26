#!/usr/bin/env python3
""" 4-tasks.py """
import asyncio
from typing import List

# Importer la fonction task_wait_random du module 3-tasks
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute la fonction task_wait_random n fois
       avec un délai maximum de max_delay.

    Retourne une liste des temps d'attente
       pour chaque exécution de task_wait_random.
    """
    list = []
    for _ in range(n):
        # Ajouter le résultat de task_wait_random à la liste
        list.append(task_wait_random(max_delay))
    # Retourner la liste des temps d'attente dans l'ordre d'achèvement
    return [await i for i in asyncio.as_completed(list)]
