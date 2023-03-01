"""Librarian"""

from library import Library
from student import Student
from datetime import datetime


class Librarian:
    """Deals with operations between students and library"""

    def __init__(self, library: Library) -> None:

        self.library = library

    def registrate(self, student: Student):

        self.library.registrate(student)

    def add_book(self, book: str, info: dict):

        self.library.add_book(book, info)

    def remove_book(self, book: str):

        self.library.remove_book(book)

    def print_student(self, student: Student):
        """Prints the chosen, registrated student's data"""

        print(
            "Name: {}\nClass: {}\nBalance: ${}\nLoaned books: {}".format(
                student.student_name,
                student.year,
                student.balance,
                self.library.data[student.student_name]["loaned_books"],
            )
        )

    def process_loan_request(self, student: Student, books: list):

        self.library.process_loan_request(student, books)

    def process_return_request(self, student: Student, books: list):

        self.library.process_return_request(student, books)

    def print_collection(self):
        """Prints the collection of the library"""

        print(self.library.collection)

    def print_registrated(self):
        """Prints the registrated students"""

        print(self.library.data)
