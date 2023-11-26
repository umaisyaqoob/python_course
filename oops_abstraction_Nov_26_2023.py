class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

class User:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.issued_books = []

    def issue_book(self, cook):
        if cook.availability > 0:
            cook.availability -= 1
            self.issued_books.append(cook.title)
            print(f"{self.name} has issued the book: {cook.title}")
        else:
            print("Sorry, the book is not available right now.")

    def return_book(self, book):
        if book.title in self.issued_books:
            book.availability += 1
            self.issued_books.remove(book.title)
            print(f"{self.name} has returned the book: {book.title}")
        else:
            print("You did not issue this book.")

# Creating instances of Book and User
math_book = Book("Maths", "Muhammad Umais", 5)
ali_user = User("Ali Raza", 5678)

# Issuing and returning books
ali_user.issue_book(math_book)
ali_user.return_book(math_book)

# Checking book availability after issuing and returning
print(f"{math_book.title} availability: {math_book.availability}")
