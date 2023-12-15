from datetime import time, timedelta
from DeliveryPackage import DeliveryPackage, Status
from Utils import get_distance_traveled, get_time_traveled
from DistanceMatrix import DistanceMatrix

#Truck class
class Truck:
    id : type(int)
    capacity : type(int)
    speed : type(int)
    load : type(int)
    packages : type(list)
    mileage : type(int)
    address_id : type(int)
    depart_time : type(time)
    time : type(time)
    has_priority_packages : type(bool)

    # __init__ Constructor
    def __init__(self, id, capacity=16, speed=18, address_id=0, depart_time=time(8, 0), packages=None, mileage=0, load=None, has_priority_packages=True  ):
        if packages is None:
            packages = []
        if load is None:
            load = len(packages)
        self.id = id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address_id = address_id
        self.depart_time = depart_time
        self.packages = packages
        self.time = depart_time
        self.has_priority_packages = True

    # load a package into the truck
    def load_package(self, idx, hash_table):
        self.packages.append(idx)
        self.load += 1
        package = hash_table.get(idx)
        package.set_truck_id(self.id)
        hash_table.update(idx, package)

    # string representation of the truck
    def __str__(self): 
        return f"Truck: {self.id} | Packages: {self.load} | Mileage:{self.mileage} miles"

    # Getters for the truck attributes
    def get_depart_time(self):
        return self.depart_time
    
    # depart the truck and set the status of the packages to enroute
    def depart(self, hash_table, time):
        self.depart_time = time
        self.load = len(self.packages)
        for package_id in self.packages:
            package = hash_table.get(package_id)
            package.status = Status.enroute

    # get the list of undelivered packages Ids
    def get_undelivered_packages(self, hash_table):
        undelivered_packages = []
        for package_id in self.packages:
            if hash_table.get(package_id).get_status() == Status.enroute:
                undelivered_packages.append(package_id)
        return undelivered_packages
    
    def get_undelivered_packages_addresses(self, undelivered_packages, hash_table):
        addresses = []
        for package_id in undelivered_packages:
            addresses.append(hash_table.get(package_id).address_id)
        return addresses
    
    # deliver a single package
    def deliver_package(self, package_id, hash_table):
        package = hash_table.get(package_id)
        distance = DistanceMatrix.get_distance_between_addresses(self.address_id, package.address_id) 
        package.set_status_to_delivered()
        self.address_id = package.address_id
        hash_table.update(package_id, package)
        self.load -= 1
        self.mileage += distance
        minutes_traveled = get_time_traveled(distance, self.speed)
        self.time = self.time+timedelta(minutes=minutes_traveled)


    # travel for a given time
    def travel_for_time_in_min(self, min):
        self.time = self.time+timedelta(minutes=min)
        distance_traveled = get_distance_traveled(self.speed, min)
        self.mileage += distance_traveled
    
    # set the current address of the truck
    def set_address_id(self, address_id):
        self.address_id = address_id
    
    # check, update, and return the priority packages
    def get_priority_packages(self, hash_table):
        priority_packages = []
        if(self.has_priority_packages == False):
            return priority_packages
        for package_id in self.packages:
            if hash_table.get(package_id).get_status() == Status.enroute:
                priority_packages.append(package_id)
        if (len(priority_packages) == 0):
            self.has_priority_packages = False
        return priority_packages