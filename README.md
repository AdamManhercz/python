# Library demo - OOP practice

The repository contains the files of the separate classes of Library, Librarian, Student, Book, Account and custom Exceptions, furthermore the main.py file for execution.

## Library class - library.py

Contains the most essential data of the library:

- data about the registrated students and book collection

## Librarian - librarian.py

Enables and carries out all possible interactions or actions between a student and the library, including:

- executes student registration
- creates student account
- management of student and library data in the database of the library.

## Student - student.py

Summarizes any demands or actions that a student might have towards the library:

- provides private information for registration
- requests book loan
- requests book return
- deposits money on account balance

## Account - account.py

Created during the registrations process:

- contains student data
- balance
- loaned books

## Custom Exceptions - error.py

Contain the customed Exceptions for library rules, such as:

- negative balance
- requested book not available
- too much loaned books at the time



