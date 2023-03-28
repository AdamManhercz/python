"""Execution"""

from library import Library
from old.librarian import Librarian
from old.student import Student


if __name__ == "__main__":

    library = Library()

    librarian = Librarian(library)

    tom = Student("Tom Jones", 2022)
    sue = Student("Sue Thomas", 2021, 50)
    carl = Student("Carl Johnson", 2022, -20)
    danny = Student("Danny DeVito", 2023)

    # add books to the library
    librarian.add_book(
        "Harry Potter", {"author": "J.K. Rowling", "release": 1997, "genre": "fantasy"}
    )
    librarian.add_book(
        "Storytelling",
        {"author": "Carmine Gallo", "release": 2016, "genre": "social science"},
    )
    librarian.add_book(
        "Lord of the Rings",
        {"author": "J.R.R. Tolkien", "release": 1954, "genre": "fantasy"},
    )

    # registrate students
    librarian.registrate(tom)
    librarian.registrate(sue)
    librarian.registrate(carl)

    # Tom's loan request
    tom_books = tom.loan_book()

    # Librarian reviews the loan request
    librarian.process_loan_request(tom, tom_books)

    # Librarian prints Tom's data
    librarian.print_student(tom)

    # Tom brought back the loaned items(s)
    tom_returned_books = tom.return_book()

    # Librarian reviews the return process
    librarian.process_return_request(tom, tom_returned_books)
