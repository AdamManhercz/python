from library import Library
from librarian import Librarian
from student import Student


if __name__ == "__main__":

    library = Library()  # initiate library instance

    librarian = Librarian()

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
        "Lord of the rings",
        {"author": "J.R.R. Tolkien", "release": 1997, "genre": "fantasy"},
    )

    # registrate students
    librarian.registrate(tom)
    librarian.registrate(sue)
    librarian.registrate(carl)

    # Tom's loan request
    tom_books, tom_loan_date = tom.loan_book()

    # Librarian reviews the loan request
    librarian.process_loan_request(tom, tom_books, tom_loan_date)

    # Librarian prints Tom's data
    librarian.print_student(tom)

    # Tom brought back the loaned items(s)
    tom_returned_books, tom_return_date = tom.return_book()

    # Librarian reviews the return process
    librarian.process_return_request(tom, tom_returned_books, tom_return_date)

    danny_books, danny_loan_date = danny.loan_book()

    librarian.process_loan_request(danny, danny_books, danny_loan_date)
