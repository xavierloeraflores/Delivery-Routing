from datetime import time

class Truck:
    id : type(int)
    capacity : type(int)
    speed : type(int)
    load : type(int)
    packages : type(list)
    mileage : type(int)
    address_id : type(int)
    depart_time : type(time)

    def __init__(self, id, capacity=16, speed=18, address_id=0, depart_time=time(8, 0), packages=None, mileage=0, load=0  ):
        if packages is None:
            packages = []
        self.id = id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address_id
        self.depart_time = depart_time
        self.packages = packages

    def set_address_id(self, address_id):
        self.address_id = address_id
    
            