# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from Utils import print_red, print_yellow, print_blue, print_green, convert_time_str_to_time
from HashTable import HashTable
from Package import PackageList
from Truck import Truck
from DeliveryPackage import DeliveryPackage
from DistanceMatrix import DistanceMatrix
from System import System

def delivery_routing_system(time=None):
    load_packages()
    delivery_algorithm(System.truck1, time)
    delivery_algorithm(System.truck2, time)
    delivery_algorithm(System.truck3, time)
    System.print_system()

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
    truck.depart(System.hash_table, time)
    next_package_id = identify_next_package(truck)
    while((time == None or time >truck.time) and next_package_id != None):
        truck.deliver_package(next_package_id, System.hash_table)
        next_package_id = identify_next_package(truck)
    truck.return_to_hub()

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



# Main program
class Main:
    print_green("Package Delivery Routing Program")
    finish_program = False

    while not finish_program:
        System.create_system()
        finish_program = interface_loop()
    
    print_red("Closing Program")