"""Library demo
Info:
- Book registry
- Student registration, library account
- Deposit money on account 
- Daily fine $1 after late
- Max loan period: 1 month
- Max books: 10

Operations:
- add books to library
- remove books from library
- student loans book
- student returns book
- student deposit money on account
"""

from dataclasses import dataclass, field


@dataclass
class Library:
    """Creates the operations of the library"""

    collection: list = field(default_factory=list)
    accounts: list = field(default_factory=list)
