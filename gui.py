import tkinter as tk
from tkinter import messagebox

from models.book import Book
from data_structures.linked_list import LinkedList
from algorithms.linear_search import linear_search


books = LinkedList()


class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        title = tk.Label(
            root,
            text="Library Management System",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)

        # ISBN
        tk.Label(form_frame, text="ISBN").grid(row=0, column=0, padx=5, pady=5)
        self.isbn_entry = tk.Entry(form_frame)
        self.isbn_entry.grid(row=0, column=1, padx=5, pady=5)

        # Title
        tk.Label(form_frame, text="Title").grid(row=1, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(form_frame)
        self.title_entry.grid(row=1, column=1, padx=5, pady=5)

        # Author
        tk.Label(form_frame, text="Author").grid(row=2, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(form_frame)
        self.author_entry.grid(row=2, column=1, padx=5, pady=5)

        # Year
        tk.Label(form_frame, text="Year").grid(row=3, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(form_frame)
        self.year_entry.grid(row=3, column=1, padx=5, pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Add Book",
            width=15,
            command=self.add_book
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Display Books",
            width=15,
            command=self.display_books
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Search Book",
            width=15,
            command=self.search_book
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Remove Book",
            width=15,
            command=self.remove_book
        ).grid(row=0, column=3, padx=5)

        self.output = tk.Text(root, width=90, height=20)
        self.output.pack(pady=10)

    def add_book(self):
        try:
            isbn = self.isbn_entry.get()
            title = self.title_entry.get()
            author = self.author_entry.get()
            year = int(self.year_entry.get())

            book = Book(isbn, title, author, year)
            books.append(book)

            messagebox.showinfo("Success", "Book added successfully!")

            self.clear_entries()

        except ValueError:
            messagebox.showerror("Error", "Year must be a number")

    def display_books(self):
        self.output.delete(1.0, tk.END)

        current = books.head

        if current is None:
            self.output.insert(tk.END, "No books found.\n")
            return

        while current:
            self.output.insert(tk.END, str(current.data) + "\n")
            current = current.next

    def search_book(self):
        isbn = self.isbn_entry.get()

        book = linear_search(books, isbn)

        if book:
            messagebox.showinfo("Book Found", str(book))
        else:
            messagebox.showwarning(
                "Not Found",
                f"No book found with ISBN {isbn}"
            )

    def remove_book(self):
        isbn = self.isbn_entry.get()

        current = books.head

        while current:
            if current.data.isbn == isbn:
                books.remove(current.data)

                messagebox.showinfo(
                    "Success",
                    f"Book with ISBN {isbn} removed"
                )

                return

            current = current.next

        messagebox.showwarning(
            "Not Found",
            f"No book found with ISBN {isbn}"
        )

    def clear_entries(self):
        self.isbn_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)


root = tk.Tk()
app = LibraryGUI(root)
root.mainloop()