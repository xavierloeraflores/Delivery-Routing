# Node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# HashTable class
class HashTable:
    # Constructor w/ initial capacity of 40 packages
    def __init__(self, cap=40):
        self.cap = cap
        self.size = 0
        self.table = []
        for _ in range(cap):   
            self.table.append(None)

    # hash_key() returns the hashed key
    def hash_key(self, key):
        hashed = hash(key) % self.cap
        return hashed

    # insert() inserts a new node into the table
    def insert(self, key, value):
        hashed_index = self.hash_key(key)
        key_value_node = Node(key, value)
        if self.table[hashed_index] == None:
            self.table[hashed_index] = key_value_node
        else:
            cur = self.table[hashed_index]
            while cur.next != None:
                cur = cur.next
            cur.next = key_value_node
        self.size += 1

    # update() updates the value of the key
    def update(self, key, value):
        hashed_index = self.hash_key(key)
        key_value_node = Node(key, value)
        cur = self.table[hashed_index]
        while cur != None:
            if cur.key == key:
                cur.value = key_value_node.value
                return
            cur = cur.next

    # get() returns the value of the key
    def get(self, key):
        hashed_index = self.hash_key(key)
        cur = self.table[hashed_index]
        while cur != None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None