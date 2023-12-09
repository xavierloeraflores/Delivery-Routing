from HashTable import HashTable
from CSVReader import CSVReader
from Package import Package, read_packages
from Utils import print_red, print_yellow, print_blue, print_green

def main():
    new_table = HashTable(40)
    new_table.insert("Hello", "World")
    hashed_key = new_table.hash_key("Hello")
    print(hashed_key)

    print(new_table)
    print("Key:Hello | Value: ", new_table.get("Hello"))

    print('-------------------------')
    new_table.remove("Hello")
    print("Key:Hello | Value: ", new_table.get("Hello"))
    print('-------------------------')
    print('-------------------------')

    new_table.insert("Key", "OldValue")
    print("Key:Key | Value: ", new_table.get("Key"))
    new_table.update("Key", "NewValue")
    print("Key:Key | Value: ", new_table.get("Key"))
    print('-------------------------')

def test_csv_reader():
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

def test_colors():
    print_red("This text is red")
    print_yellow("This text is yellow")
    print_blue("This text is blue")
    print_green("This text is green")
if __name__ == "__main__":
    # main()
    print("*************************")
    # test_csv_reader()
    # test_packages()
    test_colors()