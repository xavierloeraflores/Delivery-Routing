# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from Utils import print_red, print_yellow, print_blue, print_green, convert_time_str_to_time
from HashTable import HashTable
from Package import Package, read_packages, raw_packages_to_packages, PackageList
from Truck import Truck
from DeliveryPackage import DeliveryPackage, Status
from DistanceMatrix import DistanceMatrix
from System import System
from Address import Address, AddressBook

def delivery_routing_system(time=None):
    load_packages()
    delivery_algorithm(System.truck1, time)
    delivery_algorithm(System.truck2, time)
    delivery_algorithm(System.truck3, time)
    System.printSystem()

def load_packages():
    packages = PackageList.packages
    for package in packages:
        delivery_package = DeliveryPackage(package)
        cur_idx = delivery_package.get_id()
        if package.is_delayed():
            System.truck3.load_package(cur_idx, System.hash_table)
        elif package.has_deadline():
            System.truck1.load_package(cur_idx, System.hash_table)
        elif package.is_truck_2():
            System.truck2.load_package(cur_idx, System.hash_table)
        else:
            if System.truck2.load<System.truck3.load:
                System.truck2.load_package(cur_idx, System.hash_table)
            else:
                System.truck3.load_package(cur_idx, System.hash_table)


def delivery_algorithm(truck, time=None):
    next_package_id = identify_next_package(truck)
    while((time == None or time >truck.time) and next_package_id != None):
        truck.deliver_package(next_package_id, System.hash_table)
        next_package_id = identify_next_package(truck)
    print_green('--------- Truck Finished ---------')

def identify_next_package(truck):
    undelivered_packages = truck.get_undelivered_packages(System.hash_table)
    current_address_id = int(truck.address_id)
    undelivered_packages_addresses = []
    for package_id in undelivered_packages:
        package = System.hash_table.get(package_id)
        address_id = int(package.address.id)
        undelivered_packages_addresses.append(address_id)
    closest_address_id = DistanceMatrix.get_closest_address(current_address_id, undelivered_packages_addresses)
    for package_id in undelivered_packages:
        package_address_id = int(System.hash_table.get(package_id).address.id)
        if package_address_id == closest_address_id:
            return package_id
    return None





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
            delivery_routing_system()
        elif choice == 2:
            time_str = input("Please enter a time in the format HH:MM \n")
            time = convert_time_str_to_time(time_str)
            delivery_routing_system(time)
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



# Main program
class Main:
    system = create_system()
    print_green("Package Delivery Routing Program")
    finish_program = False

    while not finish_program:
        System.create_system()
        finish_program = interface_loop()
    
    print_red("Closing Program")