#!/usr/bin/env python3
""" 2-measure_runtime.py """
import asyncio
import time

# Importer la fonction wait_n du module 1-concurrent_coroutines
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution moyen de la fonction wait_n pour n appels
       avec un délai maximum de max_delay.
    Retourne le temps d'exécution moyen.
    """
    # Enregistrer l'heure de début en utilisant time.perf_counter
    start = time.perf_counter()
    # Exécuter wait_n avec asyncio.run
    asyncio.run(wait_n(n, max_delay))
    # Enregistrer l'heure de fin en utilisant time.perf_counter
    end = time.perf_counter()
    # Calculer et retourner le temps d'exécution moyen
    return((end - start) / n)
