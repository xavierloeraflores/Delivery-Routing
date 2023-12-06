# Student ID:   011037676
# Name:         Xavier Alejandro Loera Flores
# Date:         12/08/2023

def get_all_packages_status_at_time(time):
    print("This function will print the status of all packages at a given time")

def get_package_status_at_time(package_id, time):
    print("This function will print the status of a given package at a given time")

def interface_loop():
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
        print("Invalid input")
    return False

class Main:
    print("Package Delivery Routing Program")
    
    finish_program = False
    while not finish_program:
        finish_program = interface_loop()
    
    print("Closing Program")