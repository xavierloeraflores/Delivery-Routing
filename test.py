from HashTable import HashTable

def main():
    newTable = HashTable(40)
    newTable.insert("Hello", "World")
    hashedKey = newTable.hash_key("Hello")
    print(hashedKey)

    print(newTable)
    print("Key:Hello | Value: ", newTable.get("Hello"))

    print('-------------------------')
    newTable.remove("Hello")
    print(newTable)
    print("Key:Hello | Value: ", newTable.get("Hello"))

if __name__ == "__main__":
    main()