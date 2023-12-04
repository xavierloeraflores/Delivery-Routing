from HashTable import HashTable
from CSVReader import CSVReader

def main():
    newTable = HashTable(40)
    newTable.insert("Hello", "World")
    hashedKey = newTable.hash_key("Hello")
    print(hashedKey)

    print(newTable)
    print("Key:Hello | Value: ", newTable.get("Hello"))

    print('-------------------------')
    newTable.remove("Hello")
    print("Key:Hello | Value: ", newTable.get("Hello"))
    print('-------------------------')
    print('-------------------------')

    newTable.insert("Key", "OldValue")
    print("Key:Key | Value: ", newTable.get("Key"))
    newTable.update("Key", "NewValue")
    print("Key:Key | Value: ", newTable.get("Key"))
    print('-------------------------')

def testCSVReader():
    csvReader = CSVReader("WGUPS Package File.xlsx")
    result = csvReader.read()
    print(result)
    for row in result:
        print(row)
    # print(csvReader.read_as_dict())

if __name__ == "__main__":
    main()
    print("*************************")
    testCSVReader()