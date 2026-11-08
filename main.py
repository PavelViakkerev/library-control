import time

from algorithms.binary_search import binary_search
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.linear_search import linear_search
from algorithms.merge_sort import merge_sort
from algorithms.tree_traversal import inorder, preorder, postorder
from book import Book, load_books
from data_structures.AVL import AVLTree
from data_structures.BST import BST
from data_structures.hash_table import HashTable
from data_structures.linked_list import LinkedList
from data_structures.queue import Queue
from data_structures.stack import Stack

CSV_PATH = "books.csv"
SLOW_SORT_LIMIT = 1000
PAGE_SIZE = 20

books = LinkedList()
bst = BST()
avl = AVLTree()
hash_table = HashTable(size=16384)
history = Stack()
borrow_queue = Queue()


def normalize_isbn(isbn):
    isbn = isbn.strip()
    if isbn.isdigit():
        isbn = isbn.zfill(10)
    return isbn


def add_to_structures(book):
    books.append(book)
    if book.isbn:
        bst.insert(book)
        avl.insert(book)
        hash_table.insert(book.isbn, book)


def load_library():
    start = time.perf_counter()
    for book in load_books(CSV_PATH):
        add_to_structures(book)
    elapsed = time.perf_counter() - start
    print(f"Loaded {len(books)} books in {elapsed:.2f} s")
    print(f"BST height: {bst.get_height()}, AVL height: {avl.get_height()}")


def print_books(book_list, limit=PAGE_SIZE):
    for book in book_list[:limit]:
        print(book)
    if len(book_list) > limit:
        print(f"... and {len(book_list) - limit} more")


def timed(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return result, (time.perf_counter() - start) * 1000


def add_book():
    isbn = normalize_isbn(input("ISBN: "))
    if hash_table.get(isbn):
        print("A book with this ISBN already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        year = int(input("Year: "))
    except ValueError:
        print("Year must be a number.")
        return
    add_to_structures(Book(isbn, title, author, year))
    history.push(f"Added: {title}")
    print(f"Book '{title}' added.")


def remove_book():
    global bst, avl
    isbn = normalize_isbn(input("ISBN of the book to remove: "))
    book = hash_table.get(isbn)
    if not book:
        print(f"No book found with ISBN {isbn}.")
        return
    books.remove(book)
    hash_table.remove(isbn)
    bst = BST()
    avl = AVLTree()
    for b in books.to_list():
        if b.isbn:
            bst.insert(b)
            avl.insert(b)
    history.push(f"Removed: {book.title}")
    print(f"Book '{book.title}' removed.")


def search_by_isbn():
    isbn = normalize_isbn(input("ISBN: "))
    sorted_by_isbn = merge_sort([b for b in books.to_list() if b.isbn], key=lambda b: b.isbn)

    results = [
        ("Linear search (LinkedList)", *timed(linear_search, books, isbn)),
        ("Binary search (array)", *timed(binary_search, sorted_by_isbn, isbn)),
        ("BST search", *timed(bst.search, isbn)),
        ("AVL tree search", *timed(avl.search, isbn)),
        ("Hash table lookup", *timed(hash_table.get, isbn)),
    ]
    for name, book, ms in results:
        print(f"{name:<28} {ms:8.3f} ms  ->  {book if book else 'not found'}")
    history.push(f"Searched ISBN: {isbn}")


def sort_books():
    print("1. Merge sort (all books)")
    print(f"2. Insertion sort (first {SLOW_SORT_LIMIT})")
    print(f"3. Bubble sort (first {SLOW_SORT_LIMIT})")
    choice = input("Algorithm: ").strip()
    book_list = books.to_list()

    if choice == "1":
        result, ms = timed(merge_sort, book_list)
        name = "Merge sort"
    elif choice == "2":
        result, ms = timed(insertion_sort, book_list[:SLOW_SORT_LIMIT])
        name = "Insertion sort"
    elif choice == "3":
        result, ms = timed(bubble_sort, book_list[:SLOW_SORT_LIMIT])
        name = "Bubble sort"
    else:
        print("Invalid choice.")
        return

    print(f"{name}: {len(result)} books in {ms:.1f} ms (by publication year)")
    print_books(result)
    history.push(f"Sorted: {name}")


def traverse_tree():
    print("1. In-order")
    print("2. Pre-order")
    print("3. Post-order")
    choice = input("Traversal: ").strip()
    traversals = {"1": ("In-order", inorder), "2": ("Pre-order", preorder), "3": ("Post-order", postorder)}
    if choice not in traversals:
        print("Invalid choice.")
        return
    name, func = traversals[choice]
    result, ms = timed(func, avl.root)
    print(f"{name} traversal of the AVL tree: {len(result)} books in {ms:.1f} ms")
    print_books(result)


def borrow_book():
    user = input("Reader name: ").strip()
    book = hash_table.get(normalize_isbn(input("Book ISBN: ")))
    if not book:
        print("Book not found.")
        return
    borrow_queue.enqueue((user, book))
    print(f"{user} queued for '{book.title}'. People in queue: {borrow_queue.size()}")


def process_queue():
    if borrow_queue.is_empty():
        print("Queue is empty.")
        return
    user, book = borrow_queue.dequeue()
    history.push(f"Lent: {book.title} -> {user}")
    print(f"Book '{book.title}' lent to {user}.")


def show_last_action():
    if history.is_empty():
        print("No actions yet.")
    else:
        print(f"Last action: {history.peek()}")


MENU = [
    ("Show books", lambda: books.display(limit=PAGE_SIZE)),
    ("Add book", add_book),
    ("Remove book", remove_book),
    ("Search by ISBN (compare algorithms)", search_by_isbn),
    ("Sort by year", sort_books),
    ("Tree traversal", traverse_tree),
    ("Join the queue for a book", borrow_book),
    ("Process queue", process_queue),
    ("Last action", show_last_action),
]


def main():
    load_library()
    while True:
        print("\n===== Library System =====")
        for i, (label, _) in enumerate(MENU, 1):
            print(f"{i}. {label}")
        print("0. Exit")

        choice = input("Choice: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        if choice.isdigit() and 1 <= int(choice) <= len(MENU):
            print()
            MENU[int(choice) - 1][1]()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
