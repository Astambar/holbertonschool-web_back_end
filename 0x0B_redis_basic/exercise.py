#!/usr/bin/env python3
"""exercice"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Décorateur qui compte le nombre de fois qu'une fonction est appelée"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Fonction wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Décorateur pour stocker l'historique des entrées
    et des sorties pour une fonction particulière
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Fonction wrapper"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result

    return wrapper


class Cache:
    """Classe Cache"""

    def __init__(self):
        """
        Initialiser l'instance Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stocker les données dans Redis en utilisant une clé aléatoire
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Obtenir les données de Redis
        et les convertir au format souhaité en utilisant fn
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Obtenir une chaîne de Redis"""
        value = self.get(key, str)
        return value

    def get_int(self, key: str) -> int:
        """Obtenir un entier de Redis"""
        value = self.get(key, int)
        return value


def replay(method: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    method_name = method.__qualname__
    inputs_key = method_name + ":inputs"
    outputs_key = method_name + ":outputs"
    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for input_str, output_str in zip(inputs, outputs):
        input_str = input_str.decode("utf-8")
        output_str = output_str.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")
