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

    # insert() inserts a new node into the table
    def insert(self, key, value):
        hashedIndex = self.hash_key(key)
        key_value_node = Node(key, value)

        if self.table[hashedIndex] == None:
            self.table[hashedIndex] = key_value_node
        else:
            cur = self.table[hashedIndex]
            while cur.next != None:
                cur = cur.next
            cur.next = key_value_node

        self.size += 1

    # get() returns the value of the key
    def get(self, key):
        hashedIndex = self.hash_key(key)
        cur = self.table[hashedIndex]

        while cur != None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None
        
    # remove() removes the node with the key
    def remove(self, key):
        hashedIndex = self.hash_key(key)
        prev = None
        cur = self.table[hashedIndex]
        
        while cur != None:
            if cur.key == key:
                if prev == None:
                    self.table[hashedIndex] = cur.next
                else:
                    prev.next = cur.next
                self.size -= 1
                return
            prev = cur
            cur = cur.next
            