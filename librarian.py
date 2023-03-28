"""
Librarian

Executes operations attached to the Library.

"""

from library import Library
from student import Student
from book import Book
from account import Account


class Librarian:
    """Deals with operations between students and library"""

    def __init__(self, library: Library) -> None:

        self.library = library

    def registrate(self, student: Student):
        """Registrates student"""

        student.account = Account(student.student_name, student.year, True)
        self.library.accounts.append(student.account)

        print("========================")
        print("{} is registrated!".format(student.student_name))
        print("========================")
        
    def add_book(self, book: Book) -> None:
        """Adds books to the library"""

        self.library.collection.append(book)
        print(f"The book {book.name} has been successfully added to the library!")

    def remove_book(self, book: Book) -> None:
        """Removes books from the library"""

        self.library.collection.remove(book)
        print(f"The book {book} has been removed from the library!")

    def print_student(self, student: Student):
        """Prints the chosen, registrated student's data"""

        if student.account != None:
            print(
                "Name: {}\nClass: {}\nBalance: ${}\nLoaned books: {}".format(
                    student.student_name,
                    student.year,
                    student.account.balance,
                    student.account.loaned_books,
                )
            )
        else:
            print(f"{student.student_name} is not registrated yet.")

    def print_collection(self):
        """Prints the collection of the library"""

        print(self.library.collection)

    def print_registrated(self):
        """Prints the registrated students"""

        print(self.library.accounts)
