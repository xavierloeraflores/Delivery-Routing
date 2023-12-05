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


    