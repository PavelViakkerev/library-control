import csv


class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_csv_row(cls, row):
        isbn = row["isbn"].strip()
        if isbn:
            isbn = isbn.zfill(10)

        year = row["original_publication_year"].strip()
        if year:
            year = int(float(year))
        else:
            year = 0

        return cls(isbn, row["title"].strip(), row["authors"].strip(), year)

    @property
    def sort_year(self):
        if self.year == 0:
            return float("inf")
        return self.year

    def __str__(self):
        year = self.year if self.year else "?"
        return f"{self.isbn or '-':<10} | {self.title} | {self.author} | {year}"


def load_books(path):
    books = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            books.append(Book.from_csv_row(row))
    return books
