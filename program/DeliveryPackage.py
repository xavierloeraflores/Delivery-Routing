from Packages import Package
from enum import Enum

class Status(Enum):
    hub = "At the Hub"
    enroute = "Enroute"
    delivered = "Delivered"

class DeliveryPackage:
    status = Status
    package = Package
    def __init__(self,  package ):
        self.package = package
        self.status = Status.hub
    def set_status_to_delivered(self):
        self.status = Status.delivered

    def set_status_to_enroute(self):
        self.status = Status.enroute
        
    def get_status(self):
        return self.status