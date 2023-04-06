"""
Represents Student intance

Provides the key attributes and operations that are essential 
for a student's registration, borrowing, and returning of books from the library.
"""

from datetime import datetime
from book import Book
from account import Account
from error import AvailabilityError, BalanceError, LoanVolumeError


class Student:
    """Creates the actions of a student"""

    def __init__(
        self, student_name: str, year: int, account: Optional[Account] = None
    ) -> None:

        self.student_name = student_name
        self.year = year
        self.account = account

    def __str__(self) -> str:

        return f"{self.student_name}, {self.year}, {self.account}"

    def deposit_money(self, money: int):
        """Student deposits money on the account"""

        self.account.balance += money
        print("========================")
        print(f"Succesfully deposited: €{money}.")

    def loan_book(self, book: Book, loan_date=datetime.now()):
        """Controlls the loan process"""

        if self.account != None:
            try:
                self.account.verify_loan_request(book)
                book.volume -= 1
                self.account.loaned_books.update({book.name: loan_date})
                print(
                    f"{self.student_name} request: {book.name} has successfully loaned."
                )
            except AvailabilityError:
                print(f"{self.student_name} request: The book is not available.")
            except BalanceError:
                print(f"{self.student_name} request: Your balance is negative.")
            except LoanVolumeError:
                print(
                    f"{self.student_name} request: You have reached maximum quantity of loaned books(10)."
                )
        else:
            print(f"{self.student_name} request: You are not registrated yet.")

    def return_book(self, book: Book, return_date=datetime.now()):
        """Handles the book return"""

        self.account.check_return_date(book, return_date)

        book.volume += 1
        self.account.loaned_books.pop(book.name)
        print(f"{self.student_name} request: {book.name} has successfully returned.")
