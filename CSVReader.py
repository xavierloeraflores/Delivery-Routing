import csv


class CSVReader:
    def __init__(self, filename):
        self.filename = filename
    def readC(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            return [row for row in reader]

    def read_as_dictC(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]


    def read(self):
        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rows = []
            for row in reader:
                rows.append(row)
            return rows

    def read_as_dict(self):
        with open(self.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]