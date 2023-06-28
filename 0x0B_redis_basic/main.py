#!/usr/bin/env python3
"""Test"""
from exercise import Cache, replay

cache = Cache()

# Test store method
key = cache.store("foo")
print(key)

# Test get method
value = cache.get(key)
print(value)

# Test get_str method
value = cache.get_str(key)
print(value)

# Test get_int method
key = cache.store(42)
value = cache.get_int(key)
print(value)

# Test count_calls decorator
cache.store("bar")
cache.store("baz")
print(cache.get(cache.store.__qualname__))

# Test call_history decorator
inputs_key = cache.store.__qualname__ + ":inputs"
outputs_key = cache.store.__qualname__ + ":outputs"
inputs = cache._redis.lrange(inputs_key, 0, -1)
outputs = cache._redis.lrange(outputs_key, 0, -1)
print(f"inputs: {inputs}")
print(f"outputs: {outputs}")

# Test replay function
replay(cache.store)
