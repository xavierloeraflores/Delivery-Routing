from HashTable import HashTable

def main():
    newTable = HashTable(40)
    newTable.insert("Hello", "World")
    hashedKey = newTable.hash_key("Hello")
    print(hashedKey)

    print(newTable)

if __name__ == "__main__":
    main()