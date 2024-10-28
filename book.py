"""Represents a book instance"""

from dataclasses import dataclass


@dataclass
class Book:

    title: str
    author: str
    volume: int
