"""Library demo"""

""" 
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

    collection: dict = field(default_factory=dict)
    registrated: dict = field(default_factory=dict)

    def registrate(self, student: object):
        """Student registration"""

        # Creates the dictionary about the student's data for the library
        # Dict -> Name: Class, Balance, Loan informations
        student = student.__dict__

        self.registrated[student["student_name"]] = {
            "class": student["year"],
            "balance": student["balance"],
            "loaned_books": {},
        }

        print("========================")
        print(
            "{} from class of {} is registrated!\nYour library balance: €{}".format(
                student["student_name"], student["year"], student["balance"]
            )
        )

    def add_book(self, book: str, info: dict) -> None:
        """Add books to the library"""

        self.collection[book] = info

    def remove_book(self, book: str) -> None:
        """Remove books from the library"""

        self.collection.pop(book)
