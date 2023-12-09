from datetime import time

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

    # __init__ Constructor
    def __init__(self, id, capacity=16, speed=18, address_id=0, depart_time=time(8, 0), packages=None, mileage=0, load=None  ):
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
        self.address = address_id
        self.depart_time = depart_time
        self.packages = packages

    # string representation of the truck
    def __str__(self): 
        return f"Truck: {self.id} | Packages: {self.load} | Mileage:{self.mileage} miles"

    # Getters for the truck attributes
    def get_depart_time(self):
        return self.depart_time


    # set the current address of the truck
    def set_address_id(self, address_id):
        self.address_id = address_id