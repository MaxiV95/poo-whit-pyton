# Aggregation

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author

class Library:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

book1 = Book("One Hundred Years of Solitude", "Gabriel García Márquez")
book2 = Book("1984", "George Orwell")

library = Library("Central Library")

library.add_book(book1)
library.add_book(book2)

for book in library.books:
    print(f"Book: {book.title}, Author: {book.author}")