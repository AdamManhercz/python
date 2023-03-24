class Student:
    """Creates the actions of a student"""

    def __init__(self, student_name: str, year: int, balance: int = 0) -> None:

        self.student_name = student_name
        self.year = year
        self.balance = balance
        

    @staticmethod
    def student_input():
        """Enables on-fly registration"""

        return Student(
            input("Please, enter your name: "),
            int(input("Which year did you begin attending university: ")),
        )

    def deposit_money(self, money: int):
        """Student deposits money on the account"""

        self.balance += money

        print("========================")
        print(f"Succesfully deposited: €{money}.")
        print(f"{self.student_name}'s balance: €{self.balance}")

    def loan_book(self, books:list):
        """Gathers data on the books that have been lent out as well as the date that the loan would start."""

        booksnum = int(
            input(f"Hi, {self.student_name}! How many books would you like to loan?: ")
        )

        book_list = []
        for i in range(booksnum):

            book = input("Please, enter the title of the book: ")
            book_list.append(book)

        return book_list

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

        return book_list
