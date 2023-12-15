from Truck import Truck
from HashTable import HashTable
from DeliveryPackage import DeliveryPackage
from Package import read_packages, raw_packages_to_packages, PackageList

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
        System.truck3 = Truck(3)
        raw_packages = read_packages()
        packages = raw_packages_to_packages(raw_packages)
        for package in packages:
            delivery_package = DeliveryPackage(package)
            cur_idx = delivery_package.get_id()
            System.hash_table.insert(cur_idx, delivery_package)
    @staticmethod
    def printSystem():
        print(System.truck1)
        print(System.truck2)
        print(System.truck3)
        for package in PackageList.packages:
            delivery_package = System.hash_table.get(package.get_id())
            delivery_package.print()