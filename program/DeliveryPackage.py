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
