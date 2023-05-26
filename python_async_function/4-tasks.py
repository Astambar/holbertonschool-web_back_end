#!/usr/bin/env python3
""" 4-tasks.py """
import asyncio
from typing import List

# Importer la fonction task_wait_random du module 3-tasks
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute la fonction task_wait_random n fois avec
      un délai maximum de max_delay.

    Retourne une liste des temps d'attente
      pour chaque exécution de task_wait_random.
    """

    # Créer une liste de tâches en utilisant une compréhension de liste
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Attendre l'achèvement de toutes les tâches en utilisant asyncio.gather
    wait_times = await asyncio.gather(*tasks)
    # Retourner la liste des temps d'attente
    return wait_times
