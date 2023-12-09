from CSVReader import CSVReader
from datetime import time

# Read the package list from the CSV file
def read_packages():
    reader = CSVReader("PackageFile.csv")
    rows = reader.read()
    packages = []
    for idx, row in enumerate(rows):
        if idx != 0:
            packages.append(row)
    return packages

# Package class for the package objects raw data
class Package:
    def __init__(self, row):
        self.id = row[0]
        self.address = row[1]
        self.city = row[2]
        self.state = row[3]
        self.zip = row[4]
        self.deadline = row[5]
        self.weight = row[6]
        self.notes = row[7]
    
    # string representation of the package
    def __str__(self):
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes}"

    # Getters for the package attributes

    # Get the package id
    def get_id(self):
        return self.id
    
    # Get the package address
    def get_address(self):
        return self.address
    
    # Get the package city
    def get_city(self):
        return self.city
    
    # Get the package state
    def get_state(self):
        return self.state
    
    # Get the package zip
    def get_zip(self):
        return self.zip
    
    # Get the package deadline
    def get_deadline(self):
        return self.deadline
    
    # Get the package weight
    def get_weight(self):
        return self.weight
    
    # Get the package notes
    def get_notes(self):
        return self.notes

    # Get the deadline as a time object
    def get_deadline_as_time(self):
        time_str = self.deadline.split(" ")[0]
        if self.deadline == "EOD":
            return None
        hours = int(time_str.split(":")[0])
        minutes = int(time_str.split(":")[1])
        return time(hours, minutes)

    # Boolean check for deadline
    def has_deadline(self):
        return self.deadline != "EOD"
    
    # Boolean check for notes
    def has_notes(self):
        return self.notes != ""
    
    # Boolean check for delayed package
    def is_delayed(self):
        return self.notes == "Delayed on flight---will not arrive to depot until 9:05 am"

    # Boolean check for truck 2
    def is_truck_2(self):
        return self.notes == "Can only be on truck 2"
    
    # Boolean check for wrong address
    def has_wrong_address(self):
        return self.notes == "Wrong address listed"
    
    # Boolean check for must be delivered with
    def is_bundled(self):
        return "Must be delivered with" in self.notes
