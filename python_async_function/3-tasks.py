#!/usr/bin/env python3
""" 3-tasks.py """
import asyncio

# Importer la fonction wait_random du module 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio pour exécuter la fonction
       wait_random avec un délai maximum de max_delay.
    Retourne la tâche créée.
    """
    # Créer et retourne la tâche en appelant directement wait_random
    return asyncio.create_task(wait_random(max_delay))
