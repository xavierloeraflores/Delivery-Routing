capacity = 40

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    # Constructor w/ initial capacity of 40 packages
    def __init__(self, cap=capacity):
        self.cap = cap
        self.size = 0
        self.table = []
        for i in range(cap):
            self.table.append(None)
    
    # length of the table
    def __len__(self):
        return self.size
    
    # string representation of the table
    def __str__(self):
        return str(self.table)

    
    # hash_key() returns the hashed key
    def hash_key(self, key):
        hashed = hash(key) % self.cap
        return hashed    
