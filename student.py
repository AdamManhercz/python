"""
Represents Student intance

Provides the key attributes and operations that are essential 
for a student's registration, borrowing, and returning of books from the library.
"""

from datetime import datetime
from typing import Optional
from account import Account
from error import AvailabilityError, BalanceError, LoanVolumeError


class Student:
    """Creates the actions of a student"""

    def __init__(
        self, student_name: str, year: int, account: Optional[Account] = None
    ) -> None:

        self.name = student_name
        self.year = year
        self.account = account

    def __str__(self) -> str:

        if self.account != None:
            return f"{self.name}, {self.year}, {self.account}"
        return f"{self.name}, {self.year}, has no library account"
    
    @property
    def student_info(self) -> None:
        """Print current library-related student info"""
        print(f"Name: {self.name}")
        print(f"Class: {self.year}")
        print(f"Balance: ${self.account.balance}")
        print(f"Loaned books: {self.account.loaned_books}")

    def deposit_money(self, money: int) -> None:
        self.account.balance += money
        print("========================")
        print(f"Succesfully deposited: €{money}.")

    def loan_book(self, title: str, loan_date=datetime.now()) -> None:
        """Controlls the loan process"""
        if self.account != None:
            try:
                book = self.account.verify_loan_request(title)
                book.volume -= 1
                self.account.loaned_books.update({title: loan_date})
                print(f"{self.name}: {book.title} has successfully loaned.")
            except AvailabilityError:
                print(f"{self.name}: The book is not available.")
            except BalanceError:
                print(f"{self.name}: Your balance is negative.")
            except LoanVolumeError:
                print(f"{self.name}: Maximum quantity of loaned books exceeded(10).")
        else:
            print(f"{self.name} - You are not registrated yet.")

    def return_book(self, title: str, return_date=datetime.now()) -> None:
        """Handles the book return"""
        check = self.account.check_return_date(title, return_date)
        if check:
            book = self.account.get_book(title)
            book.volume += 1
            self.account.loaned_books.pop(title)
            print(f"{self.name} request: {title} has successfully returned.")
