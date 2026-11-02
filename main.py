from models.book import Book
from data_structures.linked_list import LinkedList
from algorithms.linear_search import linear_search

books = LinkedList()

while True:
    print("\n===== Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Exit")
  

    choice = input("Choose: ")

    if choice == "1":
        isbn = input("ISBN: ")
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        books.append(Book(isbn, title, author, year))
        print(f"Book '{title}' added successfully.")

    elif choice == "2":
        print("\n===== Book List =====")
        books.display()

    elif choice == "5":
        print("Exiting the program.")
        break
    elif choice == "3":
        isbn_to_remove = input("Enter ISBN of the book to remove: ")
        current = books.head
        while current:
            if current.data.isbn == isbn_to_remove:
                books.remove(current.data)
                print(f"Book with ISBN {isbn_to_remove} removed.")
                break
            current = current.next
        else:
            print(f"No book found with ISBN {isbn_to_remove}.")
    elif choice == "4":
        isbn_to_search = input("Enter ISBN of the book to search: ")
        found_book = linear_search(books, isbn_to_search)
        if found_book:
            print(f"Book found: {found_book}")
        else:
            print(f"No book found with ISBN {isbn_to_search}.")