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
            self.library.registrated[self.student_name]["loaned_books"],
        )

    def deposit_money(self, money: int):
        """Student deposit on the account"""

        self.balance += money

        print("========================")
        print(f"You succesfully deposit €{money}.\nYour balance: €{self.balance}")

    def loan_book(self, books: list, date: str):
        """Loaning process"""
        """Argument "books" type is list if the loan request contains several books """

        # checks the name in the registration system and the student balance
        if not self.student_name in self.library.registrated or self.balance < 0:

            return f"{self.student_name} is not registrated in the system yet or your balance is negative. Please contact with the reception"

        # checks the number of the loan request
        elif len(books) > 10:

            return f"Maximum number of loan request is 10!\n Your request number: {len(books)}"

        for book in books:

            loaned = []  # collect the available book
            if book in self.library.collection:

                loaned.append(book)  # add the available book to the list

                # register the loan details(book and date) the library side
                self.library.registrated[self.student_name]["loaned_books"][
                    book
                ] = self.library.collection[book]

                # records the loan date
                self.library.registrated[self.student_name]["loaned_books"][book][
                    "loan_date"
                ] = datetime.strptime(date, "%Y-%m-%d")

                # remove the book temporarely from the library
                self.library.remove_book(book)

            else:

                print("========================")
                print(f"The book {book} is not available!")

        print("========================")
        print(f"Successfully loaned:{loaned}")

    def return_book(self, books: list, date: str):
        """Book returning process"""
        """Argument "books" type is list if the returning process contains several books """

        for book in books:

            if book in self.library.registrated[self.student_name]["loaned_books"]:

                # start date of the loan
                loan_date = self.library.registrated[self.student_name]["loaned_books"][
                    book
                ]["loan_date"]
                # return date
                return_date = datetime.strptime(date, "%Y-%m-%d")

                diff = (return_date - loan_date).days

                # remove the loan_date element from the loaned book
                self.library.registrated[self.student_name]["loaned_books"][book].pop(
                    "loan_date"
                )

                # book gets back to the library
                self.library.add_book(
                    book,
                    self.library.registrated[self.student_name]["loaned_books"][book],
                )

                # loaned book and its loan date is getting deleted from the system
                self.library.registrated[self.student_name]["loaned_books"].pop(book)

                # if the loaning time exceeds the 30 day rule
                if diff > 30:

                    self.balance -= diff

                    print("========================")
                    print(
                        f"Due to the exceeding of the 30 day return limit your balance is charged with €{diff}!\
                        \nYour account balance is €{self.balance}."
                    )

            else:
                print("========================")
                print("The book {book} has not been loaned yet!")

        print("========================")
        print("Return is successfully processed!")


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
