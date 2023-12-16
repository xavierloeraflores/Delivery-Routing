# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from Utils import print_red, print_yellow, print_blue, print_green, convert_time_str_to_time
from Package import PackageList
from DeliveryPackage import DeliveryPackage
from DistanceMatrix import DistanceMatrix
from System import System

# delivery routing system
def delivery_routing_system(time=None):
    load_packages()
    truck1_time = delivery_algorithm(System.truck1, time)
    truck2_time = delivery_algorithm(System.truck2, time)
    if truck1_time < truck2_time:
        System.truck3.set_depart_time(truck1_time)
    else:
        System.truck3.set_depart_time(truck2_time)
    delivery_algorithm(System.truck3, time)
    System.print_system()

# load the packages into the trucks
def load_packages():
    packages = PackageList.packages
    for package in packages:
        delivery_package = DeliveryPackage(package)
        cur_idx = delivery_package.get_id()
        if package.is_delayed() or cur_idx == 9:
            System.truck3.load_package(cur_idx, System.hash_table)
        elif package.has_deadline() or package.is_bundled() or cur_idx == 19:
            System.truck1.load_package(cur_idx, System.hash_table)
        elif package.is_truck_2():
            System.truck2.load_package(cur_idx, System.hash_table)
        else:
            if System.truck2.load<System.truck3.load:
                System.truck2.load_package(cur_idx, System.hash_table)
            else:
                System.truck3.load_package(cur_idx, System.hash_table)


def delivery_algorithm(truck, time=None):
    truck.attempt_depart(System.hash_table, time)
    next_package_id = identify_next_package(truck)
    while((time == None or time >truck.time) and next_package_id != None):
        truck.deliver_package(next_package_id, System.hash_table)
        next_package_id = identify_next_package(truck)
    truck.return_to_hub()
    return truck.time

def identify_next_package(truck):
    contains_wrong_address_package = False
    undelivered_packages = truck.get_undelivered_packages(System.hash_table)
    current_address_id = int(truck.address_id)
    undelivered_packages_addresses = []
    for package_id in undelivered_packages:
        if package_id == 9:
            contains_wrong_address_package = True
        else:
            package = System.hash_table.get(package_id)
            address_id = int(package.address.id)
            undelivered_packages_addresses.append(address_id)
    closest_address_id = DistanceMatrix.get_closest_address(current_address_id, undelivered_packages_addresses)
    for package_id in undelivered_packages:
        package_address_id = int(System.hash_table.get(package_id).address.id)
        if package_address_id == closest_address_id:
            return package_id
    if contains_wrong_address_package and truck.load == 1:
        return 9
    return None





# Main interface loop that will run until the user chooses to exit
def interface_loop():
    print_blue("=====================================================")
    print_yellow("Please choose an option. Enter number and press enter.")
    print("0. Exit")
    print("1. Get completed delivery times and truck mileages")
    print("2. Get all packages's status and truck mileages at a given time")
    try:
        choice = int(input("Please choose an option:"))
        if choice not in range(0, 4) or choice == 0:
            return True
        elif choice == 1:
            print_yellow("Running delivery routing system")
            delivery_routing_system()
        elif choice == 2:
            time_str = input("Please enter a time in the format HH:MM \n")
            time = convert_time_str_to_time(time_str)
            print_yellow("Running delivery routing system until time: "+time_str)
            delivery_routing_system(time)
    except ValueError:
        print_red("Invalid input")
        return False
    return False



# Main program
class Main:
    print_green("Package Delivery Routing Program")
    finish_program = False

    while not finish_program:
        System.create_system()
        finish_program = interface_loop()
    
    print_red("Closing Program")