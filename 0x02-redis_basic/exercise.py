#!/usr/bin/env python3
"""
Module contains a `Cashe` class.

Stores an instance of the `Redis client`.
"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class."""

    def __init__(self):
        """Instance of Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """Generates a random key."""

        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
