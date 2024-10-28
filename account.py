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
    account_status: bool
    balance: int = 0
    loaned_books: dict = field(default_factory=dict)

    def check_balance(self):
        """Checks student's balance"""

        if self.balance < 0:
            raise BalanceError

    def check_book_availability(self, book: Book):

        if book.volume == 0:
            raise AvailabilityError

    def check_loaned_books_volume(self):
        """Ckeck the number of loaned books"""

        if len(self.loaned_books) > 10:
            raise LoanVolumeError

    def verify_loan_request(self, book: Book):

        self.check_balance()
        self.check_book_availability(book)
        self.check_loaned_books_volume()

    def check_return_date(self, book: Book, return_date: datetime):
        """Determines whether a late return charge is applicable"""

        if book.title in self.loaned_books:
            late = (return_date - self.loaned_books[book.title]).days
            charge = late - 30
            if charge > 0:
                self.balance -= charge
                print(f"{self.student_name}: You missed the 30 days loan limit.")
                print(
                    f"{self.student_name}: Your balance has been charged with €{charge}."
                )
        else:
            print(f"The {book.title} has not been loaned out yet")
