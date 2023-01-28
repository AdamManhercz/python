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

from dataclasses import dataclass
from datetime import datetime
from library import Library


@dataclass
class Student:
    """Creates the actions of the students"""

    student_name: str
    year: int
    library: Library
    balance: int = 0

    def __str__(self) -> str:
        """Displays the actual information about the student"""

        return "Name: {}\nClass: {}\nBalance: ${}\nLoaned books: {}".format(
            self.student_name,
            self.year,
            self.balance,
            self.library.data[self.student_name]["loaned_books"],
        )

    def deposit_money(self, money: int):
        """Student deposit on the account"""

        self.balance += money

        print("========================")
        print(f"You succesfully deposit €{money}.\nYour balance: €{self.balance}")

    def loan_book(self, books: list, loan_date: str):
        """Loaning process"""

        # checks the name in the registration system and the student balance
        if not self.student_name in self.library.data or self.balance < 0:

            return f"{self.student_name} is not data in the system yet or your balance is negative.\
                        Please contact with the reception"

        # checks the number of the loan request
        elif len(books) > 10:

            return f"Maximum number of loan request is 10!\n Your request number: {len(books)}"

        for book in books:

            loaned = []  # collect the available book
            if book in self.library.collection:

                loaned.append(book)  # add the available book to the list

                # register the loaned book's details
                self.library.data
                [self.student_name]
                ["loaned_books"]
                [book] = self.library.collection[book]

                # records the loan date
                self.library.data
                [self.student_name]
                ["loaned_books"]
                [book]["loan_date"] = datetime.strptime(loan_date, "%Y-%m-%d")

                # remove the book from the library
                self.library.remove_book(book)

            else:
                print("========================")
                print(f"The book {book} is not available!")

        print("========================")
        print(f"Successfully loaned:{loaned}")

    def return_book(self, books: list, return_date: str):
        """Book returning process"""

        for book in books:

            if book in self.library.data[self.student_name]["loaned_books"]:

                self.check_dates(book, return_date)

                # remove the loan_date element from the loaned book
                self.library.data
                [self.student_name]["loaned_books"][book].pop("loan_date")

                # book gets back to the library
                self.library.add_book(
                    book,
                    self.library.data[self.student_name]["loaned_books"][book],
                )

                # loaned book and its loan date is getting deleted from the system
                self.library.data
                [self.student_name]["loaned_books"].pop(book)

            else:
                print("========================")
                print(f"The book {book} has not been loaned yet!")

        print("========================")
        print("Return is successfully processed!")

    def check_dates(self, book: str, return_date: str):
        """Checks if there is any fine for late returning"""

        loan_date = self.library.data
        [self.student_name]["loaned_books"][book]["loan_date"]

        return_date = datetime.strptime(return_date, "%Y-%m-%d")

        diff = (return_date - loan_date).days

        # if the loaning time exceeds the 30 day rule
        if diff > 30:

            # the actual fine for the late return
            charge = diff - 30

            self.balance -= charge

            print("========================")
            print(
                f"Due to the exceeding of the 30 day return limit your balance is charged with €{charge}!\
                        \nYour account balance is €{self.balance}."
            )


if __name__ == "__main__":

    library = Library()  # initiate library instance

    # add book to the library
    library.add_book("Harry Potter", {"release": 1997, "genre": "fantasy"})

    # initiate a student Tom Jerry
    tom = Student("Tom Jerry", 2023, library)

    # registrate Tom
    library.registrate(tom)

    # Tom loans book, library removes tha loaned book from collection
    tom.loan_book(["Harry Potter"], "2023-01-24")

    # Tom returns the book, if there is a charge he will be informed
    tom.return_book(["Harry Potter"], "2023-03-24")

    # display Tom account
    print(tom)

    # Tom deposits money on his account
    tom.deposit_money(59)
