# Library Control

A simple library management system in Python. It uses a real dataset of 10,000 books (`books.csv`)
to show how basic data structures and algorithms work.

## Files

| File / folder | What it contains |
|---|---|
| `main.py` | Console menu of the library |
| `book.py` | `Book` class and loading of `books.csv` |
| `books.csv` | Dataset with 10,000 books |
| `data_structures/` | Linked list, stack, queue, hash table, BST, AVL tree |
| `algorithms/` | Bubble, insertion and merge sort; linear and binary search; tree traversals |
| `tests.py` | Tests for all data structures and algorithms |
| `benchmark.ipynb` | Time and memory comparison of the algorithms |

## How it is used in the library

- **Linked list** stores all books
- **Hash table**, **BST** and **AVL tree** find a book by ISBN
- **Stack** keeps the history of actions (last action)
- **Queue** keeps readers waiting for a book
- **Sorting algorithms** sort books by publication year
- **Tree traversals** (in-order, pre-order, post-order) walk through the AVL tree

## How to run

Run all commands from the project folder.

```
python main.py        # start the library menu
python tests.py       # run the tests
```

Open `benchmark.ipynb` in VS Code or Jupyter to see the performance analysis.
It needs `pandas` and `matplotlib`:

```
pip install pandas matplotlib
```
