import csv

# CSVReader class to read CSV files
class CSVReader:
    # initialize the CSVReader object with a filename
    def __init__(self, filename):
        self.filename = filename

    # read the CSV file
    def read(self):
        with open(self.filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            rows = []
            for row in reader:
                rows.append(row)
            return rows