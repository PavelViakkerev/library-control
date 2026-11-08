class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BST:


    def __init__(self):
        self.root = None

    def insert(self, book):
        new_node = BSTNode(book)
        if self.root is None:
            self.root = new_node
            return
        node = self.root
        while True:
            if book.isbn < node.book.isbn:
                if node.left is None:
                    node.left = new_node
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    return
                node = node.right

    def search(self, isbn):
        node = self.root
        while node:
            if isbn == node.book.isbn:
                return node.book
            node = node.left if isbn < node.book.isbn else node.right
        return None

    def get_height(self):
        return self._height(self.root)

    def _height(self, node):
        height = 0
        level = [node] if node else []
        while level:
            height += 1
            next_level = []
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            level = next_level
        return height
