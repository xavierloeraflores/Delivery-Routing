from HashTable import HashTable
from CSVReader import CSVReader
from Packages import Package, read_packages

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
    package_file = CSVReader("PackageFile.csv")
    packages = package_file.read()
    for row in packages:
        print(row)
    
    print("-------------------------")
    
    distance_table = CSVReader("DistanceTable.csv")
    distances = distance_table.read()
    for row in distances:
        print(row)

def test_packages():
    packages = read_packages()
    for row in packages:
        print(row)
    print("-------------------------")
    for row in packages:
        package = Package(row)
        print(package)

if __name__ == "__main__":
    # main()
    print("*************************")
    # testCSVReader()
    test_packages()