from models.book import Book
from data_structures.linked_list import LinkedList

books = LinkedList()

while True:
    print("\n===== Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Exit")

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

    elif choice == "3":
        print("Exiting the program.")
        break
    elif choice == "4":
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