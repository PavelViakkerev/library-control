class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.isbn} | {self.title} | {self.author} | {self.year}"
book1 = Book("001", "Python Basics", "John Smith", 2020)
book2 = Book("002", "Data Structures", "Jane Doe", 2022)