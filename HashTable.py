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
    
    def hash_value(self, key):
        hashedValue = hash(key)
        return hashedValue    

def main():
    newTable = HashTable(40)
    hashedValue = newTable.hash_value("Hello")
    print(hashedValue)

if __name__ == "__main__":
    main()