from Truck import Truck
from HashTable import HashTable
from DeliveryPackage import DeliveryPackage
from Package import read_packages, raw_packages_to_packages, PackageList
from datetime import datetime
from Utils import print_blue

class System:
    truck1 = None
    truck2 = None
    truck3 = None
    hash_table = None

    # create the system
    @staticmethod
    def create_system():
        System.hash_table = HashTable(40)
        System.truck1 = Truck(1)
        System.truck2 = Truck(2)
        truck3_depart_time = datetime(year=2000, month=1, day=1,hour=9,minute=5,second=0)
        System.truck3 = Truck(3, truck3_depart_time)
        raw_packages = read_packages()
        packages = raw_packages_to_packages(raw_packages)
        for package in packages:
            delivery_package = DeliveryPackage(package)
            cur_idx = delivery_package.get_id()
            System.hash_table.insert(cur_idx, delivery_package)
    @staticmethod
    def print_system():
        print_blue(System.truck1)
        print_blue(System.truck2)
        print_blue(System.truck3)
        print("Total Distance Traveled: "+str(System.truck1.mileage+System.truck2.mileage+System.truck3.mileage)+ " miles")
        for package in PackageList.packages:
            delivery_package = System.hash_table.get(package.get_id())
            delivery_package.print()