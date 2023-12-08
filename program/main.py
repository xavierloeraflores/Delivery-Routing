# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

from PrintColor import print_red, print_yellow, print_blue, print_green

def get_all_packages_status_at_time(time):
    print("This function will print the status of all packages at a given time")

def get_package_status_at_time(package_id, time):
    print("This function will print the status of a given package at a given time")

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

class Main:
    print_green("Package Delivery Routing Program")
    
    finish_program = False
    while not finish_program:
        finish_program = interface_loop()
    
    print_red("Closing Program")