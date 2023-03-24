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
from datetime import datetime
from student import Student


@dataclass
class Library:
    """Creates the operations of the library"""

    collection: dict = field(default_factory=dict)
    accounts: dict = field(default_factory=dict)

    def add_book(self, book: str, info: dict) -> None:
        """Adds books to the library"""

        self.collection[book] = info
        print(f"The book {book} has been successfully added to the library!")

    def remove_book(self, book: str) -> None:
        """Removes books from the library"""

        self.collection.pop(book)
        print(f"The book {book} has been removed from the library!")

    def registrate(self, student: Student):
        """Registrates student"""
        # Creates the dictionary about the student's data for the library

        student = student.__dict__

        self.accounts[student["student_name"]] = {
            "year": student["year"],
            "balance": student["balance"],
            "loaned_books": dict(),
        }
        print("========================")
        print("{} is registrated!".format(student["student_name"]))
        print("Your library balance: €{}".format(student["balance"]))
        print("========================")

    def check_account(self, student: Student):
        """Checks if the student is registrated"""

        if not student.student_name in self.accounts:
            raise KeyError

    def check_book(self, student: Student, books: list):
        """Checks each book and the amount of books that student has loaned"""

        if len(self.accounts[student.student_name]["loaned_books"]) > 10:
            raise Exception
        for book in books:
            if not book in self.collection:
                raise Exception

    def check_balance(self, student: Student):
        """Checks the balance of the student"""

        if student.balance < 0:
            raise ValueError

    def check_request_data(self, student: Student, books: list):
        """Compiles all the relevant constraints to the loaning process"""

        self.check_account(student)
        self.check_balance(student)
        self.check_book(student, books)

    def process_book(
        self, student: Student, books: list[str], loan_date=datetime.now()
    ):
        """Carries out the loaning if all the requiremnets are fulfilled"""
        loaned = []
        for book in books:
            book_info = self.collection[book]
            # book gets recorded as a loaned book at the student
            self.accounts[student.student_name]["loaned_books"].update({book: book_info})

            ## records the loan date
            self.accounts[student.student_name]["loaned_books"].setdefault(book, {})
            book_date_section = self.accounts[student.student_name]["loaned_books"][book]
            book_date_section.setdefault("loan_date", loan_date)

            loaned.append(book)
            # remove the book from the library
            self.remove_book(book)
        print(f"{student.student_name} has successfully loaned:{loaned}")

    def process_loan_request(
        self, student: Student, books: list, loan_date=datetime.now()
    ):
        """Summarizes the loan process"""
        try:
            self.check_request_data(student, books)

        except KeyError:
            print("You are not registrated!")
            student = student.student_input()
            self.registrate(student)
            books = student.loan_book()
            self.process_loan_request(student, books)

        except ValueError:
            deposit_question = input("Negative balance! Want to make a deposit? Y/N: ")
            while deposit_question != "Y":
                deposit_question = input(
                    "Negative balance! Want to make a deposit? Y/N: "
                )
            # student adds money to the account
            money = int(input("How much money would you like to deposit?"))
            student.deposit_money(money)

            # loan process can be restarted
            books = student.loan_book()
            self.process_loan_request(student, books)

        except Exception:
            print("Please edit your loan request!")
            print("The book is unavailable or you have 10+ loaned books!")
            books = student.loan_book()
            self.process_loan_request(student, books)

        else:
            self.process_book(student, books)

    def process_return_request(
        self, student: Student, books: list, return_date=datetime.now()
    ):
        """Book returning process"""
        returned_books = []
        for book in books:
            if book in self.accounts[student.student_name]["loaned_books"]:

                self.check_dates(student, book, return_date)
                # remove the loan_date element from the loaned book
                self.accounts[student.student_name]["loaned_books"][book].pop("loan_date")
                # book gets back to the library
                self.add_book(
                    book, self.accounts[student.student_name]["loaned_books"][book]
                )
                # loaned book and its loan date is getting deleted from the system
                self.accounts[student.student_name]["loaned_books"].pop(book)

                returned_books.append(book)
            else:
                print("========================")
                print(f"The book {book} has not been loaned yet!")
        print("========================")
        print(f"Successfully returned: {returned_books}!")

    def check_dates(self, student: Student, book: str, return_date: str):
        """Determines if there is a late return penalty"""

        loan_date = self.accounts[student.student_name]["loaned_books"][book]["loan_date"]
        diff = (return_date - loan_date).days

        # if the loaning time exceeds the 30 day rule
        if diff > 30:
            # the actual fine for the late return
            charge = diff - 30
            student.balance -= charge
            print("========================")
            print(f"Student: {student.student_name}")
            print(f"Charge: €{charge}")
            print("Issue: 30 day return restriction being exceeded!")
            print(f"Your account balance is €{student.balance}.")
