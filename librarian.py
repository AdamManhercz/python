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

        student.account = Account(student.name, student.year, True)
        self.library.accounts.append(student.account)
        
        print("========================")
        print("{} is registrated!".format(student.name))
        print("========================")

    def add_book(self, book: Book) -> str:
        """Adds books to the library"""
        
        self.library.collection.append(book)
        print(f"The book {book.title} has been successfully added to the library!")

    def remove_book(self, book: Book) -> str:
        """Removes books from the library"""

        self.library.collection.remove(book)
        return f"The book {book.title} has been removed from the library!"

    def check_student(self, student: Student) -> str:
        """Prints the chosen, registrated student's data"""

        if student.account == None:
            print(f"{student.name} is not registrated yet.") 
        else:
            student.student_info          

    def print_collection(self) -> str:
        """Prints the collection of the library"""

        print(self.library.collection)

    def print_registrated(self) -> str:
        """Prints the registrated students"""

        print(self.library.accounts)
