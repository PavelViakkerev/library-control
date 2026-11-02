class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    
    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    
    def remove(self, data):
        if self.head is None:
            return

        
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next