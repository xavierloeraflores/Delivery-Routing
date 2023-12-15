# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from Utils import print_red, print_yellow, print_blue, print_green, convert_time_str_to_time
from HashTable import HashTable
from Package import Package, read_packages, raw_packages_to_packages
from Truck import Truck
from DeliveryPackage import DeliveryPackage, Status
from DistanceMatrix import DistanceMatrix

def identify_next_package(truck, hash_table):
    print("This function will return the next package to be delivered")
    undelivered_packages = truck.get_undelivered_packages(hash_table)
    current_address_id = truck.get_address_id()
    undelivered_packages_addresses = []
    closest_address_id = DistanceMatrix.get_closest_address(current_address_id, undelivered_packages_addresses)
    for package_id in undelivered_packages:
        package = hash_table.get(package_id)
        if package.address_id == closest_address_id:
            return package_id

def get_completed_delivery_times_and_truck_mileages(system):
    print("This function will print the completed delivery times and truck mileages")
    _hash_table = system[0]
    _packages = system[1]
    _truck1 = system[2]
    _truck2 = system[3]
    _truck3 = system[4]

def get_all_packages_status_at_time(time_str, system):
    _time = convert_time_str_to_time(time_str)
    _hash_table = system[0]
    _packages = system[1]
    _truck1 = system[2]
    _truck2 = system[3]
    _truck3 = system[4]

    print("This function will print the status of all packages at a given time")
    print("Time:", _time)

def get_package_status_at_time(package_id, time):
    print("This function will print the status of a given package at a given time")

# Main interface loop that will run until the user chooses to exit
def interface_loop(system):
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
            get_completed_delivery_times_and_truck_mileages(system)
        elif choice == 2:
            time_str = input("Please enter a time in the format HH:MM \n")
            get_all_packages_status_at_time(time_str, system)
        elif choice == 3:
            print("Option 3")
    except ValueError:
        print_red("Invalid input")
    return False

def create_system():
    hash_table = HashTable(40)
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)
    raw_packages = read_packages()
    packages = raw_packages_to_packages(raw_packages)
    for package in packages:
        delivery_package = DeliveryPackage(package)
        cur_idx = delivery_package.get_id()
        hash_table.insert(cur_idx, delivery_package)
        if package.is_delayed():
            truck3.load_package(cur_idx, hash_table)
        elif package.has_deadline():
            truck1.load_package(cur_idx, hash_table)
        elif package.is_truck_2():
            truck2.load_package(cur_idx, hash_table)
        else:
            if truck2.load<truck3.load:
                truck2.load_package(cur_idx, hash_table)
            else:
                truck3.load_package(cur_idx, hash_table)
    return [hash_table, packages, truck1, truck2, truck3]

def print_system(system):
    _hash_table = system[0]
    _packages = system[1]
    _truck1 = system[2]
    _truck2 = system[3]
    _truck3 = system[4]
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
    system = create_system()
    print_system(system)
    print_green("Package Delivery Routing Program")
    finish_program = False
    while not finish_program:
        finish_program = interface_loop(system)
    
    print_red("Closing Program")