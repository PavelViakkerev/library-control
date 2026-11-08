import math
import random
import unittest

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


def make_book(isbn, year=2000):
    return Book(isbn, "Title " + isbn, "Author", year)


def years(book_list):
    return [b.year for b in book_list]


def isbns(book_list):
    return [b.isbn for b in book_list]


class TestBook(unittest.TestCase):
    def test_restores_leading_zeros(self):
        row = {"isbn": "439023483", "title": "The Hunger Games", "authors": "Suzanne Collins",
               "original_publication_year": "2008.0"}
        book = Book.from_csv_row(row)
        self.assertEqual(book.isbn, "0439023483")
        self.assertEqual(book.year, 2008)

    def test_missing_isbn_and_year(self):
        row = {"isbn": "", "title": "No data", "authors": "Someone", "original_publication_year": ""}
        book = Book.from_csv_row(row)
        self.assertEqual(book.isbn, "")
        self.assertEqual(book.year, 0)
        self.assertEqual(book.sort_year, float("inf"))

    def test_load_csv(self):
        books = load_books("books.csv")
        self.assertEqual(len(books), 10000)
        self.assertEqual(books[0].title, "The Hunger Games (The Hunger Games, #1)")


class TestLinkedList(unittest.TestCase):
    def test_empty(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertEqual(ll.to_list(), [])
        self.assertFalse(ll.remove("x"))

    def test_append_keeps_order(self):
        ll = LinkedList()
        for x in [1, 2, 3]:
            ll.append(x)
        self.assertEqual(ll.to_list(), [1, 2, 3])
        self.assertEqual(len(ll), 3)

    def test_remove_head_middle_tail(self):
        ll = LinkedList()
        for x in [1, 2, 3, 4]:
            ll.append(x)
        self.assertTrue(ll.remove(1))
        self.assertTrue(ll.remove(3))
        self.assertTrue(ll.remove(4))
        self.assertEqual(ll.to_list(), [2])
        ll.append(5)
        self.assertEqual(ll.to_list(), [2, 5])

    def test_remove_missing(self):
        ll = LinkedList()
        ll.append(1)
        self.assertFalse(ll.remove(99))
        self.assertEqual(ll.to_list(), [1])


class TestStack(unittest.TestCase):
    def test_last_in_first_out(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())

    def test_empty_stack_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()


class TestQueue(unittest.TestCase):
    def test_first_in_first_out(self):
        q = Queue()
        for x in ["a", "b", "c"]:
            q.enqueue(x)
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.dequeue(), "a")
        self.assertEqual(q.dequeue(), "b")
        self.assertEqual(q.size(), 1)

    def test_empty_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.dequeue())


class TestHashTable(unittest.TestCase):
    def test_insert_and_get(self):
        t = HashTable()
        t.insert("0439023483", "Hunger Games")
        self.assertEqual(t.get("0439023483"), "Hunger Games")
        self.assertIsNone(t.get("missing"))

    def test_update_existing_key(self):
        t = HashTable()
        t.insert("a", 1)
        t.insert("a", 2)
        self.assertEqual(t.get("a"), 2)
        self.assertEqual(len(t), 1)

    def test_remove(self):
        t = HashTable()
        t.insert("a", 1)
        self.assertTrue(t.remove("a"))
        self.assertIsNone(t.get("a"))
        self.assertFalse(t.remove("a"))

    def test_collisions(self):
        t = HashTable(size=1)
        for i in range(100):
            t.insert(f"key{i}", i)
        self.assertEqual(len(t.buckets[0]), 100)
        for i in range(100):
            self.assertEqual(t.get(f"key{i}"), i)
        t.remove("key50")
        self.assertIsNone(t.get("key50"))
        self.assertEqual(t.get("key51"), 51)

    def test_same_key_same_bucket(self):
        t = HashTable(size=64)
        self.assertEqual(t._hash("0439023483"), t._hash("0439023483"))


class TestBST(unittest.TestCase):
    def test_empty(self):
        tree = BST()
        self.assertIsNone(tree.search("1"))
        self.assertEqual(tree.get_height(), 0)
        self.assertEqual(inorder(tree.root), [])

    def test_insert_and_search(self):
        tree = BST()
        for isbn in ["5", "3", "8", "1", "4"]:
            tree.insert(make_book(isbn))
        self.assertEqual(tree.search("4").isbn, "4")
        self.assertIsNone(tree.search("9"))

    def test_sorted_input_makes_tall_tree(self):
        tree = BST()
        for i in range(100):
            tree.insert(make_book(f"{i:03d}"))
        self.assertEqual(tree.get_height(), 100)


class TestAVL(unittest.TestCase):
    def test_empty(self):
        tree = AVLTree()
        self.assertIsNone(tree.search("1"))
        self.assertEqual(tree.get_height(), 0)

    def test_sorted_input_stays_balanced(self):
        tree = AVLTree()
        n = 1000
        for i in range(n):
            tree.insert(make_book(f"{i:04d}"))
        self.assertLessEqual(tree.get_height(), 1.45 * math.log2(n + 2))
        self.assertEqual(isbns(inorder(tree.root)), [f"{i:04d}" for i in range(n)])

    def test_every_node_balanced(self):
        tree = AVLTree()
        keys = [f"{i:04d}" for i in range(500)]
        random.Random(1).shuffle(keys)
        for k in keys:
            tree.insert(make_book(k))

        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            right = check(node.right)
            self.assertLessEqual(abs(left - right), 1)
            return 1 + max(left, right)

        check(tree.root)

    def test_search(self):
        tree = AVLTree()
        for isbn in ["10", "20", "30", "40", "50"]:
            tree.insert(make_book(isbn))
        self.assertEqual(tree.search("30").isbn, "30")
        self.assertIsNone(tree.search("35"))


class TestTraversals(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        for isbn in ["4", "2", "6", "1", "3", "5", "7"]:
            self.tree.insert(make_book(isbn))

    def test_inorder(self):
        self.assertEqual(isbns(inorder(self.tree.root)), ["1", "2", "3", "4", "5", "6", "7"])

    def test_preorder(self):
        self.assertEqual(isbns(preorder(self.tree.root)), ["4", "2", "1", "3", "6", "5", "7"])

    def test_postorder(self):
        self.assertEqual(isbns(postorder(self.tree.root)), ["1", "3", "2", "5", "7", "6", "4"])

    def test_empty_tree(self):
        self.assertEqual(preorder(None), [])
        self.assertEqual(postorder(None), [])

    def test_single_node(self):
        tree = BST()
        tree.insert(make_book("1"))
        self.assertEqual(isbns(inorder(tree.root)), ["1"])
        self.assertEqual(isbns(preorder(tree.root)), ["1"])
        self.assertEqual(isbns(postorder(tree.root)), ["1"])


class TestSorting(unittest.TestCase):
    sorts = {"bubble": bubble_sort, "insertion": insertion_sort, "merge": merge_sort}

    def check(self, input_years):
        expected = sorted(input_years)
        for name, sort in self.sorts.items():
            with self.subTest(algorithm=name):
                data = [make_book(str(i), y) for i, y in enumerate(input_years)]
                self.assertEqual(years(sort(data)), expected)

    def test_empty(self):
        self.check([])

    def test_one_element(self):
        self.check([2000])

    def test_random(self):
        rng = random.Random(7)
        self.check([rng.randint(1800, 2020) for _ in range(200)])

    def test_already_sorted(self):
        self.check(list(range(1900, 2000)))

    def test_reversed(self):
        self.check(list(range(2000, 1900, -1)))

    def test_duplicates(self):
        self.check([2001, 1999, 2001, 1999, 2001])

    def test_negative_years(self):
        self.check([2008, -750, 1597, -430])

    def test_unknown_year_goes_last(self):
        for name, sort in self.sorts.items():
            with self.subTest(algorithm=name):
                data = [make_book("a", 0), make_book("b", 1990), make_book("c", 1850)]
                self.assertEqual(years(sort(data)), [1850, 1990, 0])

    def test_stable(self):
        for name, sort in self.sorts.items():
            with self.subTest(algorithm=name):
                data = [make_book("first", 2000), make_book("x", 1990), make_book("second", 2000)]
                self.assertEqual(isbns(sort(data)), ["x", "first", "second"])


class TestSearching(unittest.TestCase):
    def setUp(self):
        self.books = [make_book(f"{i:03d}") for i in range(0, 100, 2)]
        self.linked = LinkedList()
        for b in self.books:
            self.linked.append(b)

    def test_binary_search_first_middle_last(self):
        self.assertEqual(binary_search(self.books, "000").isbn, "000")
        self.assertEqual(binary_search(self.books, "050").isbn, "050")
        self.assertEqual(binary_search(self.books, "098").isbn, "098")

    def test_binary_search_missing(self):
        self.assertIsNone(binary_search(self.books, "051"))
        self.assertIsNone(binary_search(self.books, "999"))

    def test_binary_search_empty(self):
        self.assertIsNone(binary_search([], "000"))

    def test_linear_search(self):
        self.assertEqual(linear_search(self.linked, "098").isbn, "098")
        self.assertIsNone(linear_search(self.linked, "051"))
        self.assertIsNone(linear_search(LinkedList(), "000"))

    def test_all_searches_agree_on_real_data(self):
        books = [b for b in load_books("books.csv") if b.isbn][:2000]
        linked = LinkedList()
        bst = BST()
        avl = AVLTree()
        table = HashTable()
        for b in books:
            linked.append(b)
            bst.insert(b)
            avl.insert(b)
            table.insert(b.isbn, b)
        array = merge_sort(books, key=lambda b: b.isbn)

        for b in random.Random(3).sample(books, 50):
            self.assertIs(linear_search(linked, b.isbn), b)
            self.assertIs(binary_search(array, b.isbn), b)
            self.assertIs(bst.search(b.isbn), b)
            self.assertIs(avl.search(b.isbn), b)
            self.assertIs(table.get(b.isbn), b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
