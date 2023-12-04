def main():
    newTable = HashTable(40)
    hashedValue = newTable.hash_value("Hello")
    print(hashedValue)

if __name__ == "__main__":
    main()