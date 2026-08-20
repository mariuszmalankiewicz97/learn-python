class Book:
    def __init__(self, title, author, year_of_publication, available=True):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.available = available

    def __str__(self):
        return f"\nTitle: {self.title}, \nAuthor: {self.author}, \nYear of publication:{self.year_of_publication}, \nAvailable: {self.available}"


class Library:
    def __init__(self):
        self.stock = {}

    def add_book(self, book):
        self.stock[book.title] = book
        return f"Book sucess add: {book}"

    def delete_book(self, book):
        if book.title in self.stock:
            del self.stock[book.title]
            return f"Book delete sucess: {book}"

    def view_books(self):
        return self.stock

    def find_book(self, title):
        if title in self.stock:
            return f"Find success: {self.stock[title]}"

    def rent_book(self, title):
        title = title.title()
        if title in self.stock and self.stock[title].available == True:
            self.stock[title].available = False
            return f"Rent success: {self.stock[title]}"

    def return_book(self, title):
        if title in self.stock and self.stock[title].available == False:
            self.stock[title].available = True
            return f"Return success: {self.stock[title]}"

    def check_available_book(self, title):
        title = title.title()
        if title in self.stock and self.stock[title].available:
            return True
        return False


library = Library()

book_1 = Book("Władca Pierścieni", "J.R.R. Tolkien", 1954)
book_2 = Book("Harry Potter", "J.K. Rowling", 1997)
book_3 = Book("Diuna", "Frank Herbert", 1965)

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.delete_book(book_1)
# print(library.view_books())
# print(library.find_book("Harry Potter"))
library.rent_book("Harry Potter")
library.return_book("Harry Potter")

print(library.check_available_book("harry Potter"))
