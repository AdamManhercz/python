from dataclasses import dataclass


@dataclass
class Student:
    """Creates the actions of a student"""

    student_name: str
    year: int
    balance: int = 0

    @staticmethod
    def student_input():
        """Enable on-fly registration"""

        return Student(
            input("Please, enter your name: "),
            int(input("Which year did you begin attending university: ")),
            int(
                input(
                    "Would you wish to add money to the balance on your account?(Optional!)"
                )
            ),
        )

    def deposit_money(self, money: int):
        """Student deposit on the account"""

        self.balance += money

        print("========================")
        print(
            f"{self.student_name} has succesfully deposited €{money}.\n{self.student_name}'s balance: €{self.balance}"
        )

    def loan_book(self):
        """Gathers data on the books that have been lent out as well as the date that the loan would start."""

        booksnum = int(
            input(f"Hi, {self.student_name}! How many books would you like to loan?: ")
        )

        book_list = []
        for i in range(booksnum):

            book = input("Please, enter the title of the book: ")
            book_list.append(book)

        loan_date = input(
            "Please, enter the date where the loan would start:(Year-month-day)"
        )
        return book_list, loan_date

    def return_book(self):
        """Gathers the data on the books that will be returned and the date of the return"""

        booksnum = int(
            input(
                f"Hi, {self.student_name}! How many books would you like to return?: "
            )
        )

        book_list = []
        for i in range(booksnum):

            book = input("Please, enter the title of the book: ")
            book_list.append(book)

        return_date = input(
            "Please, enter the day you returns your book:(Year-month-day)"
        )

        return book_list, return_date
