from Package import Package
from enum import Enum
from datetime import time
from Address import Address, get_address_by_street
from Utils import convert_time_str_to_time_extended


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
        if package.get_deadline() != "EOD":
            self.deadline = convert_time_str_to_time_extended(package.get_deadline())
        self.address = get_address_by_street(package.get_address())
    
    # get the status of the package
    def get_status(self):
        return self.status
    
    # get the package object
    def get_package(self):
        return self.package 
    
    def get_id(self):
        return self.package.get_id()
    
    # get the delivery time of the package
    def get_delivery_time(self):
        return self.delivery_time
    
    def get_status_at_time(self, time, truck):
        depart_time = truck.get_depart_time()
        if self.delivery_time is None:
            return self.status
        if depart_time < time and time < self.delivery_time:
            return Status.enroute
        if time > self.delivery_time:
            return Status.delivered
        if time < depart_time:
            return Status.hub
            
    
    # Setters

    # Sets the status of the package to delivered
    def set_status_to_delivered(self):
        self.status = Status.delivered

    # Sets the status of the package to enroute
    def set_status_to_enroute(self):
        self.status = Status.enroute

    # Sets the delivery time of the package
    def set_delivery_time(self, time, truck):
        self.delivery_time = time

    # Sets the truck id of the package
    def set_truck_id(self, truck_id):
        self.truck_id = truck_id