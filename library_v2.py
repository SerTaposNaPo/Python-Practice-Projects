from typing import Optional
import json

def main():
    library = Library()
    library.load_from_file()
    while True:
        print("=== Library ===")
        print("1. View Books")
        print("2. Add Books")
        print("3. Checkout Books")
        print("4. Return Books")
        print("5. Exit")
        answer = int(input("What is your choice : "))
        if answer == 1:
            library.list_book()
        elif answer == 2:
            print("1. Book")
            print("2. Ebook")
            print("3. Audiobook")
            book_type = int(input("Input Book Type : "))
            title = input("Input book name : ")
            author = input("Input Author : ")
            isbn = input("Input ISBN : ")
            if book_type == 1:
                book_info = Book(title, author, isbn,)
                library.add_book(book_info)
            elif book_type == 2:
                file_size = int(input("File size : "))
                book_info = Ebook(title, author, isbn, file_size)
                library.add_book(book_info)
            elif book_type == 3:
                duration = int(input("Duration : "))
                book_info = AudioBook(title, author, isbn, duration)
                library.add_book(book_info)
        elif answer == 3:
            checked_isbn = input("What is the ISBN : ")
            library.checkout_book(checked_isbn)
        elif answer == 4:
            return_isbn = input("What is the ISBN : ")
            library.return_book(return_isbn)
        elif answer == 5:
            library.save_to_file()
            break



class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def to_dict(self):
        return {
            "title" : self.title,
            "author" : self.author,
            "ISBN" : self.isbn,
            "Availability" : self.is_checked_out,
            "Type" : "Book"
        }

class Ebook(Book):
    def __init__(self, title, author, isbn, file_size_mb=0):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

    def to_dict(self):
        base_data = super().to_dict()
        base_data["File_size"] = self.file_size_mb
        base_data["Type"] = "Ebook"
        return base_data

class AudioBook(Book):
    def __init__(self, title, author, isbn, duration_minutes=0):
        super().__init__(title, author, isbn)
        self.duration_minutes = duration_minutes

    def to_dict(self):
        base_data = super().to_dict()
        base_data["Duration"] = self.duration_minutes
        base_data["Type"] = "Audiobook"
        return base_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def list_book(self):
        for book in self.books:
            print()
            print(f"Title : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN : {book.isbn}")
            print()

    def find_book(self, isbn) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def checkout_book(self, isbn):
        book = self.find_book(isbn)
        if book is None:
            print("Book not found")
            return
        if book.is_checked_out:
            print(f"{book.title} is already checked out")
            return
        book.is_checked_out = True
        print(f"{book.title} is checked out successfully")

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book is None:
            print("Book not found")
            return
        if not book.is_checked_out:
            print(f"{book.title} was not checked out")
            return
        book.is_checked_out = False
        print(f"{book.title} is returned successfully")

    def save_to_file(self):
        books_dict = []
        for book in self.books:
            new_book = book.to_dict()
            books_dict.append(new_book)
        with open("library_data.json", "w") as file:
            json.dump(books_dict, file)

    def load_from_file(self):
        try:
            with open("library_data.json", "r") as file:
                loaded_data = json.load(file)
                for book in loaded_data:
                    if book["Type"] == "Book":
                        new_book = Book(book["title"], book["author"], book["ISBN"])
                    elif book["Type"] == "Ebook":
                        new_book = Ebook(book["title"], book["author"], book["ISBN"], book["File_size"])
                    elif book["Type"] == "Audiobook":
                        new_book = AudioBook(book["title"], book["author"], book["ISBN"], book["Duration"])
                    new_book.is_checked_out = book["Availability"]
                    self.books.append(new_book)

        except FileNotFoundError:
            pass

if __name__ == "__main__":
    main()