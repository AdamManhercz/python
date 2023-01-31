"""Librarian"""


from library import Library
from student import Student
from datetime import datetime


class Librarian(Library):
    """Deals with operations between students and library"""

    def print_student(self, student: Student):
        """Prints the chosen, registrated student's data"""

        print(
            "Name: {}\nClass: {}\nBalance: ${}\nLoaned books: {}".format(
                student.student_name,
                student.year,
                student.balance,
                self.data[student.student_name]["loaned_books"],
            )
        )

    def print_collection(self):
        """Prints the collection of the library"""

        print(self.collection)

    def print_registrated(self):
        """Prints the registrated students"""

        print(self.data)

    def check_account(self, student: Student):
        """Checks if the student is registrated"""

        if not student.student_name in self.data:
            raise KeyError

    def check_book_list(self, books: list):
        """Checks each book and the length of the requested book list"""

        if len(books) > 10:
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

        self.check_book_list(books)

    def process_book(self, student: Student, books: list[str], loan_date: str):
        """Carries out the loaning if all the requiremnets are fulfilled"""

        loaned = []
        for book in books:

            book_info = self.collection[book]

            self.data[student.student_name]["loaned_books"].update({book: book_info})

            ## records the loan date
            self.data[student.student_name]["loaned_books"].setdefault(
                book, {}
            ).setdefault("loan_date", datetime.strptime(loan_date, "%Y-%m-%d"))

            loaned.append(book)

            # remove the book from the library
            self.remove_book(book)

        print(f"{student.student_name} has successfully loaned:{loaned}")

    def process_loan_request(self, student: Student, books: list, loan_date: str):
        """Summarizes the loan process"""

        try:
            self.check_request_data(student, books)

        except KeyError:

            print("You are not registrated!")
            student = student.student_input()
            self.registrate(student)

        except ValueError:
            deposit_question = input(
                "Your account balance is negative! Would you like to deposit money on your account? Y/N: "
            )

            while deposit_question != "Y":
                deposit_question = input(
                    "Your account balance is negative! Would you like to deposit money on your account? Y/N: "
                )
            else:
                money = int(input("How much money would you like to deposit?"))

                student.deposit_money(money)

                books, loan_date = student.loan_book()
                self.process_loan_request(student, books, loan_date)

        except Exception:
            print(
                "Please edit your loan request!\nMaybe a book is not available or length of request exceeds the contraint(10)!"
            )
            books, loan_date = student.loan_book()
            self.process_loan_request(student, books, loan_date)

        else:
            self.process_book(student, books, loan_date)

    def process_return_request(self, student: Student, books: list, return_date: str):
        """Book returning process"""

        returned_books = []
        for book in books:

            if book in self.data[student.student_name]["loaned_books"]:

                self.check_dates(student, book, return_date)

                # remove the loan_date element from the loaned book
                self.data[student.student_name]["loaned_books"][book].pop("loan_date")

                # book gets back to the library
                self.add_book(
                    book,
                    self.data[student.student_name]["loaned_books"][book],
                )

                # loaned book and its loan date is getting deleted from the system
                self.data[student.student_name]["loaned_books"].pop(book)

                returned_books.append(book)

            else:
                print("========================")
                print(f"The book {book} has not been loaned yet!")

        print("========================")
        print(f"{student.student_name} has successfully returned: {returned_books}!")

    def check_dates(self, student: Student, book: str, return_date: str):
        """Determines if there is a late return penalty"""

        loan_date = self.data[student.student_name]["loaned_books"][book]["loan_date"]

        return_date = datetime.strptime(return_date, "%Y-%m-%d")

        diff = (return_date - loan_date).days

        # if the loaning time exceeds the 30 day rule
        if diff > 30:

            # the actual fine for the late return
            charge = diff - 30

            student.balance -= charge

            print("========================")
            print(
                f"{student.student_name}, your balance will be charged €21 as a result of the 30 day return restriction being exceeded.!\
                        \nYour account balance is €{student.balance}."
            )
