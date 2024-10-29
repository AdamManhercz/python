"""
Represents the Student's account after registration.
Contains the essential registration the about the Student:
the name, the balance, the loaned books of the Student, 
as well as the year the Student attended at the university.
"""
from dataclasses import dataclass, field
from book import Book
from error import AvailabilityError, BalanceError, LoanVolumeError
import datetime


@dataclass
class Account:

    student_name: str
    year: int
    book_collection: list
    balance: int = 0
    loaned_books: dict = field(default_factory=dict)

    def check_balance(self):
        """Checks student's balance"""

        if self.balance < 0:
            raise BalanceError
        
    def get_book(self, title: str) -> Book:
        return next((book for book in self.book_collection if title == book.title), None)

    def check_book_availability(self, book: Book) -> None:
        if not book or book.volume == 0:
            raise AvailabilityError

    def check_loaned_books_volume(self):
        """Ckeck the number of loaned books"""

        if len(self.loaned_books) > 10:
            raise LoanVolumeError

    def verify_loan_request(self, title: str) -> Book:
        book = self.get_book(title)
        self.check_balance()
        self.check_loaned_books_volume()
        self.check_book_availability(book)
        return book

    def check_return_date(self, title: str, return_date: datetime) -> bool:
        """Determines whether a late return charge is applicable"""
        if title in self.loaned_books:
            late = (return_date - self.loaned_books[title]).days
            charge = late - 30
            if charge > 0:
                self.balance -= charge
                print(f"{self.student_name}: You missed the 30 days loan limit.")
                print(
                    f"{self.student_name}: Your balance has been charged with €{charge}."
                )
            return True
        else:
            print(f"The {title} has not been loaned out yet")
            return False
