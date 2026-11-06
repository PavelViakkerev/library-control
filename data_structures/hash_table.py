class HashTable:
    def __init__(self, size=10):
        self.table ={}
    def insert(self, key, value):
        self.table[key] = value
    def get(self, key):
        if key in self.table:
            del self.table[key]


