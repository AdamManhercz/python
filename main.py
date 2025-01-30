from student import Student
from librarian import Librarian
from library import OnlineLibrary
from book import Book
from datetime import datetime

if __name__ == "__main__":

    # initiate Library and Librarian instance
    library = OnlineLibrary()
    librarian = Librarian(library)

    # initiate Students
    tom = Student("Tom Jones", 2022)
    lucy = Student("Lucy Liu", 2023)
    sue = Student("Sue Thomas", 2021)
    carl = Student("Carl Johnson", 2022)

    # initiate Book intances
    book1 = Book("Harry Potter", "JK Rowling", 3)
    book2 = Book("Vuk", "Fekete István", 2)
    book3 = Book("Zen", "Én", 1)

    # add the book to the library's collection
    librarian.add_book(book1)
    librarian.add_book(book2)
    librarian.add_book(book3)

    # registrate Students
    librarian.registrate(tom)
    librarian.registrate(lucy)
    librarian.registrate(sue)

    # show Student attributes
    print(tom)
    print(carl)

    # loan requests
    tom.loan_book("Harry Potter")
    tom.loan_book("Vuk")
    carl.loan_book("Vuk")
    lucy.loan_book("Zen")
    sue.loan_book("Zen")

    # take a look at the changes after loans
    librarian.check_student(tom)
    librarian.print_collection()

    # return loaned book
    tom.return_book("Harry Potter")
    lucy.return_book("Zen", datetime(2025, 5, 28))

    print(lucy)

    # loan request with negative balance
    lucy.loan_book("Zen")

    # check the collection regarding book volumes
    #librarian.print_collection()

    # deposit money on the account balance
    #tom.deposit_money(20)
    #print(tom)
