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
from datetime import datetime
from library import Library


@dataclass
class Student:
    """Creates the actions of the students"""

    name: str
    year: int
    info: Library
    loaned_books: dict = field(default_factory=dict)
    balance: int = 0

    def __str__(self) -> str:
        """Displays the actual information about the student"""

        return f"Name: {self.name}\nClass: {self.year}\nBalance: ${self.balance}\nLoaned books: {self.loaned_books}"

    def deposit_money(self, money: int):
        """Student deposit on the account"""

        self.balance += money

        print(f"You succesfully deposit ${money}.\nYour balance: ${self.balance}")

    def loan_book(self, books: list, date: str):
        """Loaning process"""
        """Argument "books" type is list if the loan request contains several books """

        # checks the name in the registration system and the student balance
        if not self.name in self.info.registrated or (self.balance < 0):

            return f"{self.name} is not registrated in the system yet or your balance is negative. Please contact with the reception"

        # checks the number of the loan request
        elif len(books) > 10:

            return f"Maximum number of loan request is 10!\n Your request number: {len(books)}"

        for book in books:

            loaned = []  # collect the available book
            if book in self.info.collection:

                loaned.append(book)  # add the available book to the list

                # register the loan details(book and date) the student side
                self.loaned_books[book] = self.info.collection[book]
                self.loaned_books[book]["loan_date"] = datetime.strptime(
                    date, "%Y-%m-%d"
                )
                # register the loan details(book and date) the library side
                self.info.registrated[self.name]["loaned_books"][
                    book
                ] = self.info.collection[book]
                self.info.registrated[self.name]["loaned_books"][book][
                    "loan_date"
                ] = datetime.strptime(date, "%Y-%m-%d")

                # remove the book temporarely from the library
                self.info.remove_book(book)

            else:

                print(f"The book {book} is not available!")

        print(f"Successfully loaned:{loaned}")

    def return_book(self, books: list, date: str):  # argument "books"
        """Book returning process"""
        """Argument "books" type is list if the returning process contains several books """

        for book in books:

            if book in self.info.registrated[self.name]["loaned_books"]:

                loan_date = self.info.registrated[self.name]["loaned_books"][book][
                    "loan_date"
                ]  # start date of the loan
                return_date = datetime.strptime(date, "%Y-%m-%d")  # return date

                diff = (
                    return_date - loan_date
                ).days  # difference between start and return date

                # remove the loan_date element from the loaned book
                self.info.registrated[self.name]["loaned_books"][book].pop("loan_date")

                # book get back to the library
                self.info.add_book(
                    book, self.info.registrated[self.name]["loaned_books"][book]
                )

                # loaned book and its loan date is getting deleted from the system
                self.info.registrated[self.name]["loaned_books"].pop(book)

                # if the loaning time exceeds the 30 day rule
                if diff > 30:

                    self.balance -= diff
                    print(
                        f"Due to the exceeding of the 30 return limit your balance is charged with ${diff}!"
                    )
                    print(f"Your account balance is ${self.balance}.")
            else:
                print("The book {book} has not been loaned yet!")

        print("Return is successfully processed!")


if __name__ == "__main__":

    library = Library()  # initiate library instance

    # add book to the library
    library.add_book("Harry Potter", {"release": 2001, "genre": "fantasy"})

    # initiate a student Tom Jerry
    tom = Student("Tom Jerry", 2023, library)

    # registrate Tom
    library.registrate(tom)

    # Tom loans book, library removes tha loaned book from collection
    tom.loan_book(["Harry Potter"], "2023-01-24")

    # Tom returns the book, if there is a charge he will be informed
    tom.return_book(["Harry Potter"], "2023-03-24")

    # Tom deposits money on his account
    tom.deposit_money(59)
