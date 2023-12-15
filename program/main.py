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

def deliveryRoutingSystem(time=None):
    print("This function will return a list of trucks and their packages")
    loadPackages()
    print(System.truck1.packages)
    print(System.hash_table.get(34).status)
    deliveryAlgorithm(System.truck1, time)
    print(System.hash_table.get(34).status)
    print(System.truck1.packages)
    deliveryAlgorithm(System.truck2, time)
    deliveryAlgorithm(System.truck3, time)
    System.printSystem()

def loadPackages():
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


def deliveryAlgorithm(truck, time=None):
    next_package_id = identify_next_package(truck)
    while((time == None or time >truck.time) and next_package_id != None):
        truck.deliver_package(next_package_id, System.hash_table)
        next_package_id = identify_next_package(truck)
    print_green('--------- Truck Finished ---------')

def print34(idx, str):
    if(idx == 34):
        print_red(str)
def print22(idx, str):
    if(idx == 22):
        print_red(str)
def identify_next_package(truck):
    undelivered_packages = truck.get_undelivered_packages(System.hash_table)
    print(undelivered_packages)
    # print_yellow("Undelivered packages: " + str(undelivered_packages))
    current_address_id = int(truck.address_id)
    # print_yellow("Current address id: " + str(current_address_id))
    undelivered_packages_addresses = []
    for package_id in undelivered_packages:
        package = System.hash_table.get(package_id)
        # print_yellow("----Package Address: " + str(package.address))
        # print_yellow("Raw Address: " + str(package.package))
        address_id = int(package.address.id)
        undelivered_packages_addresses.append(address_id)
        print34(package_id, current_address_id)
    # print_yellow("Undelivered packages addresses: " + str(undelivered_packages_addresses))
    # print_blue(undelivered_packages_addresses)
    closest_address_id = DistanceMatrix.get_closest_address(current_address_id, undelivered_packages_addresses)
    print22(current_address_id,closest_address_id )
    # print_blue(undelivered_packages_addresses)
    # print_blue('***********')
    for package_id in undelivered_packages:
        # print_green("Package id: " + str(package_id))
        package_address_id = int(System.hash_table.get(package_id).address.id)
        # print_blue("Package address id: " + str(package.get_id() ))
        # print(closest_address_id, package_address_id)
        if package_address_id == closest_address_id:
            # print_green(True)
            return package_id
    return None

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



# Main program
class Main:
    system = create_system()
    print_green("Package Delivery Routing Program")
    finish_program = False
    System.create_system()

    deliveryRoutingSystem()
    while not finish_program:
        finish_program = interface_loop(system)
    
    print_red("Closing Program")