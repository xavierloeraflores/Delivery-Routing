from Utils import CSVReader

# Read the package list from the CSV file
def read_packages():
    reader = CSVReader("PackageFile.csv")
    rows = reader.read()
    packages = []
    for idx, row in enumerate(rows):
        if idx != 0:
            packages.append(row)
    return packages

def raw_packages_to_packages(raw_packages):
    packages = []
    for package in raw_packages:
        new_package = Package(package)
        packages.append(new_package)
    return packages
# Package class for the package objects raw data
class Package:
    def __init__(self, row):
        self.id = int(row[0])
        self.address = row[1]
        self.city = row[2]
        self.state = row[3]
        self.zip = row[4]
        self.deadline = row[5]
        self.weight = row[6]
        self.notes = row[7]
        if self.has_wrong_address():
            self.address = "410 S State St"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip = "84111"
    
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

# PackageList class for the package list
class PackageList:
    raw_packages = read_packages()
    packages = raw_packages_to_packages(raw_packages)