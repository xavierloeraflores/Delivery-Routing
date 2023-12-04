from HashTable import HashTable

def main():
    newTable = HashTable(40)
    hashedKey = newTable.hash_key("Hello")
    print(hashedKey)

if __name__ == "__main__":
    main()