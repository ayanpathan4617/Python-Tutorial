
class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showStatus(self):
        print(f"the total no. of books is{self.noOfBooks} books")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter")

l1.showStatus()