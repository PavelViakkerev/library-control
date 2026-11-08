class AVLNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, book):
        self.root = self._insert(self.root, book)

    def _insert(self, node, book):
        if node is None:
            return AVLNode(book)

        if book.isbn < node.book.isbn:
            node.left = self._insert(node.left, book)
        else:
            node.right = self._insert(node.right, book)

        self.update_height(node)
        b = self.balance(node)

        if b > 1 and book.isbn < node.left.book.isbn:
            return self.rotate_right(node)
        if b < -1 and book.isbn >= node.right.book.isbn:
            return self.rotate_left(node)
        if b > 1:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b < -1:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, isbn):
        node = self.root
        while node:
            if isbn == node.book.isbn:
                return node.book
            if isbn < node.book.isbn:
                node = node.left
            else:
                node = node.right
        return None

    def get_height(self):
        return self.height(self.root)
