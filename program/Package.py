from CSVReader import CSVReader


def read_packages():
    reader = CSVReader("PackageFile.csv")
    rows = reader.read()
    packages = []
    for idx, row in enumerate(rows):
        if idx != 0:
            packages.append(row)
    return packages


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
    
    def __str__(self):
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes}"

    def get_id(self):
        return self.id
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip(self):
        return self.zip
    
    def get_deadline(self):
        return self.deadline
    
    def get_weight(self):
        return self.weight
    
    def get_notes(self):
        return self.notes

    def has_deadline(self):
        return self.deadline != "EOD"
    
    def has_notes(self):
        return self.notes != ""
    
    def is_delayed(self):
        return self.notes == "Delayed on flight---will not arrive to depot until 9:05 am"

    def is_truck_2(self):
        return self.notes == "Can only be on truck 2"
    
    def has_wrong_address(self):
        return self.notes == "Wrong address listed"
    
    def is_bundled(self):
        return "Must be delivered with" in self.notes
