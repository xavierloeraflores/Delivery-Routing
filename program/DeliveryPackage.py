from Package import Package
from enum import Enum
from datetime import time
from Address import Address, AddressBook
from Utils import convert_time_str_to_time_extended, print_green, print_yellow, print_red


# Status Enum that represents the status of the package
class Status(Enum):
    hub = "At the Hub"
    enroute = "Enroute"
    delivered = "Delivered"

# DeliveryPackage class
class DeliveryPackage:
    status = Status
    package = Package
    delivery_time = time
    deadline = time
    address_id = Address
    truck_id = int

    # __init__ Constructor
    def __init__(self,  package ):
        self.package = package
        self.status = Status.hub
        self.delivery_time = None
        self.deadline = None
        self.truck_id = None
        if package.deadline != "EOD":
            self.deadline = convert_time_str_to_time_extended(package.deadline)
        self.address = AddressBook.get_address_by_street(package.address)

    # Print the package information
    def print(self):
        package_string = ""
        package_string += f"Package: {str(self.package.id).zfill(2)}"
        package_string += f"| Truck: {self.truck_id}  "
        package_string += f"| Status: {self.status.value}\t"
        if(self.status == Status.delivered):
            package_string += f"| Delivered: {str(self.delivery_time.hour).zfill(2)}:{str(self.delivery_time.minute).zfill(2)}:{str(self.delivery_time.second).zfill(2)}\t"
        else:
            package_string += "| Delivered:\t\t"
        if(self.package.has_deadline()):
            package_string += f"| Deadline: {str(self.deadline.hour).zfill(2)}:{str(self.deadline.minute).zfill(2)}:{str(self.deadline.second).zfill(2)}"
        else:
            package_string += "| Deadline: \t"
        package_string += f"\t| Weight: {str(self.package.weight).zfill(2)} "
        package_string += f"| Zip: {self.package.zip}"
        package_string += f" | Address: {str(self.address.street).ljust(40)}"
        package_string += f"| City: {self.package.city}"
        if(self.status == Status.delivered):
            print_green(package_string)
        elif(self.status == Status.enroute):
            print_yellow(package_string)
        else:
            print_red(package_string)
    
    # Get the package id
    def get_id(self):
        return self.package.id
    
    # Sets the status of the package to delivered
    def set_status_to_delivered(self):
        self.status = Status.delivered

    # Sets the status of the package to enroute
    def set_status_to_enroute(self):
        self.status = Status.enroute

    # Sets the delivery time of the package
    def set_delivery_time(self, time):
        self.delivery_time = time

    # Sets the truck id of the package
    def set_truck_id(self, truck_id):
        self.truck_id = truck_id