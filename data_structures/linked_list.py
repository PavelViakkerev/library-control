class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def display(self, limit=None):
        current = self.head
        shown = 0
        while current and (limit is None or shown < limit):
            print(current.data)
            current = current.next
            shown += 1

    def remove(self, data):
        prev = None
        current = self.head
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current is self.tail:
                    self.tail = prev
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def to_list(self):
        books = []
        current = self.head
        while current:
            books.append(current.data)
            current = current.next
        return books

    def __len__(self):
        return self.size
