from Package import Package
from enum import Enum
from datetime import time

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

    # __init__ Constructor
    def __init__(self,  package ):
        self.package = package
        self.status = Status.hub
        self.delivery_time = None
    
    # get the status of the package
    def get_status(self):
        return self.status
    
    # get the package object
    def get_package(self):
        return self.package 
    
    # get the delivery time of the package
    def get_delivery_time(self):
        return self.delivery_time
    
    # Setters

    # Sets the status of the package to delivered
    def set_status_to_delivered(self):
        self.status = Status.delivered

    # Sets the status of the package to enroute
    def set_status_to_enroute(self):
        self.status = Status.enroute

    # Sets the delivery time of the package
    def set_delivery_time(self, time):
        self.delivery_time = time