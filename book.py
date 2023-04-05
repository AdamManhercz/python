"""Represents a book instance"""

from dataclasses import dataclass


@dataclass
class Book:

    name: str
    author: str
    volume: int
