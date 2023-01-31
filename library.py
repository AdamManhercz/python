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
    data: dict = field(default_factory=dict)

    def registrate(self, student: object):
        """Registrates student"""

        # Creates the dictionary about the student's data for the library
        # Dict -> Name: Class, Balance, Loan informations
        student = student.__dict__

        self.data[student["student_name"]] = {
            "year": student["year"],
            "balance": student["balance"],
            "loaned_books": dict(),
        }

        print("========================")
        print(
            "{} from class of {} is registrated!\nYour library balance: €{}".format(
                student["student_name"], student["year"], student["balance"]
            )
        )
        print("========================")

    def add_book(self, book: str, info: dict) -> None:
        """Adds books to the library"""

        self.collection[book] = info

        print(f"The book {book} has been successfully added to the library!")

    def remove_book(self, book: str) -> None:
        """Removes books from the library"""

        self.collection.pop(book)

        print(f"The book {book} has been removed from the library!")
