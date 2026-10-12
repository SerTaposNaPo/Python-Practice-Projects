from typing import Optional




def main():
    library = Library()
    while True:
        print("=== Library ===")
        print("1. Add book")
        print("2. Check out a book")
        print("3. Return a book")
        print("4. View Books")
        print("5. Exit")
        answer = int(input("What do you want to do : "))
        if answer == 1:
            title = input("Input book name : ")
            author = input("Input Author : ")
            isbn = input("Input ISBN : ")
            book_info = Book(title, author, isbn)
            library.add_book(book_info)

        elif answer == 2:
            checkout_isbn = input("What is the ISBN: ")
            library.checkout_book(checkout_isbn)
        elif answer == 3:
            return_isbn = input("What is the ISBN: ")
            library.return_book(return_isbn)
        elif answer == 4:
            library.list_books()
        elif answer == 5:
            break


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def list_books(self):
        for book in self.books:
            print(f"Title : {book.title}")
            print(f"Author : {book.author}")
            print(f"ISBN : {book.isbn}")

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


if __name__ == "__main__":
    main()