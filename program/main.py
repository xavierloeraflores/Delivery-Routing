# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from PrintColor import print_red, print_yellow, print_blue, print_green
from HashTable import HashTable
from Package import Package, read_packages, raw_packages_to_packages
from Truck import Truck
from DeliveryPackage import DeliveryPackage, Status

def get_all_packages_status_at_time(time):
    print("This function will print the status of all packages at a given time")

def get_package_status_at_time(package_id, time):
    print("This function will print the status of a given package at a given time")

# Main interface loop that will run until the user chooses to exit
def interface_loop():
    print("=====================================================")
    print("Please choose an option. Enter number and press enter.")
    print("0. Exit")
    print("1. Get completed delivery times and truck mileages")
    print("2. Get all packages's status and truck mileages at a given time")
    print("3. Get specific packages's status at a given time")
    try:
        choice = int(input("Please choose an option:"))
        if choice not in range(0, 4) or choice == 0:
            return True
        elif choice == 1:
            print("Option 1")
        elif choice == 2:
            print("Option 2")
        elif choice == 3:
            print("Option 3")
    except ValueError:
        print_red("Invalid input")
    return False

def create_program_objects():
    hash_table = HashTable(40)
    raw_packages = read_packages()
    packages = raw_packages_to_packages(raw_packages)
    for package in packages:
        delivery_package = DeliveryPackage(package)
        hash_table.insert(delivery_package.get_id(), delivery_package)
        t = hash_table.get(delivery_package.get_id())
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)
    return [hash_table, packages, truck1, truck2, truck3]

def print_program_objects(program_objects):
    _hash_table = program_objects[0]
    _packages = program_objects[1]
    _truck1 = program_objects[2]
    _truck2 = program_objects[3]
    _truck3 = program_objects[4]
    print("Printing program objects")
    print_red("Hash Table:")
    print_red(_hash_table)
    print_yellow("Packages:")
    for package in _packages:
        print_yellow(package)
    print_blue(_truck1)
    print_green(_truck2)
    print_green(_truck3)
    print("End of program objects")


# Main program
class Main:
    program_objects = create_program_objects()
    print_program_objects(program_objects)
    print_green("Package Delivery Routing Program")
    
    finish_program = False
    while not finish_program:
        finish_program = interface_loop()
    
    print_red("Closing Program")