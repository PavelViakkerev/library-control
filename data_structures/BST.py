class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if self.root is None:
            self.root = BSTNode(book)
        else:
            self._insert(self.root, book)

    def _insert(self, node, book):

        if book.isbn < node.book.isbn:

            if node.left is None:
                node.left = BSTNode(book)
            else:
                self._insert(node.left, book)

        else:

            if node.right is None:
                node.right = BSTNode(book)
            else:
                self._insert(node.right, book)

    def search(self, isbn):
        return self._search(self.root, isbn)

    def _search(self, node, isbn):

        if node is None:
            return None

        if node.book.isbn == isbn:
            return node.book

        if isbn < node.book.isbn:
            return self._search(node.left, isbn)

        return self._search(node.right, isbn)