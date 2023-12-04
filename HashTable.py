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
    
    # hash_key() returns the hashed key
    def hash_key(self, key):
        hashed = hash(key) % self.cap
        return hashed    
