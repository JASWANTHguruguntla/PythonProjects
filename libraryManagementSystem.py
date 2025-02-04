class Book:
    def __init__(self,title,author,isbn):
        self.title=title 
        self.author=author
        self.isbn=isbn

    def __str__(self):
        return f"Title:{self.title},Author:{self.author},ISBN:{self.isbn}"
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Book'{book.title}' added to the library")
    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' is removed from the library")
    def search_book_by_title(self,title):
        results=[book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print("Search results")
            for book in results:
                print(book)
        else:
            print("No books found with the given title")
    def display_all_books(self):
        if self.books:
            print("Books in library")
            for book in self.books:
                print(book)
        else:
            print("No books in the library")
#Example usage 
if __name__== "__main__":
    library = Library()

    book1 = Book("The Guide", "R.K.Narayan", "978-8185986175")
    book2 = Book("Goldan", "Munshi Premchand", "978-8122200030")
    book3 = Book("The White Tiger", "Aravind Adiga", "978-1416562603")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.search_book_by_title("Goldan")

    library.remove_book("978-1416562603")
    library.display_all_books()