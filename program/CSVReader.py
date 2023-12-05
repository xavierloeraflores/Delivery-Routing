import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rows = []
            for row in reader:
                rows.append(row)
            return rows