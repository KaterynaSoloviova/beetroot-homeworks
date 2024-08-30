# Task 2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
# list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.

class Author:
    def __init__(self, name: str, country: str, birthday: str) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self) -> str:
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self) -> str:
        return f"{self.name} ({self.country}, born: {self.birthday})"


class Book:
    def __init__(self, name: str, year: int, author: Author) -> None:
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self) -> str:
        return f"Book({self.name}, {self.year}, {self.author.name})"

    def __str__(self) -> str:
        return f"'{self.name}' by {self.author.name} ({self.year})"


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author) -> list[Book]:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list[Book]:
        return [book for book in self.books if book.year == year]

    def __repr__(self) -> str:
        return f"Library({self.name}, Books: {len(self.books)}, Authors: {len(self.authors)})"

    def __str__(self) -> str:
        return f"Library '{self.name}' with {len(self.books)} books by {len(self.authors)} authors."


library = Library("The big library")
author1 = Author("Arthur Conan Doyle", "United Kingdom", 1859)
author2 = Author("Agatha Christie", "United Kingdom", 1890)
book1 = library.new_book("The Mystery of Cloomber", 1888, author1)
book2 = library.new_book("Death on the Nile", 1937, author2)
book3 = library.new_book("The Murder of Roger Ackroyd", 1926, author2)

assert len(library.books) == 3

assert (f"{author1}" == "Arthur Conan Doyle (United Kingdom, born: 1859)")
assert (f"{author1.__repr__()}" == "Author(Arthur Conan Doyle, United Kingdom, 1859)")
assert (f"{author2}" == "Agatha Christie (United Kingdom, born: 1890)")
assert (f"{library.books[0]}" == "'The Mystery of Cloomber' by Arthur Conan Doyle (1888)")
assert (f"{book1.__repr__()}" == "Book(The Mystery of Cloomber, 1888, Arthur Conan Doyle)")
assert (f"{book2}" == "'Death on the Nile' by Agatha Christie (1937)")
assert (f"{book3}" == "'The Murder of Roger Ackroyd' by Agatha Christie (1926)")
assert (f"{library}" == "Library 'The big library' with 3 books by 0 authors.")
assert (f"{library.group_by_year(1937)}" == "[Book(Death on the Nile, 1937, Agatha Christie)]")
assert (f"{library.group_by_author(author2)}" == "[Book(Death on the Nile, 1937, Agatha Christie), Book(The Murder of "
                                                 "Roger Ackroyd, 1926, Agatha Christie)]")
