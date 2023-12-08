from CSVReader import CSVReader

def read_addresses():
    reader = CSVReader("AddressList.csv")
    rows = reader.read()
    addresses = []
    for idx, row in enumerate(rows):
        if idx != 0:
            addresses.append(row)
    return addresses

def get_address_list():
    addresses = read_addresses()
    address_list = []
    idx=1
    for row in addresses:
        address = Address(idx, row[0])
        address_list.append(address)
        idx += 1
    return address_list

class Address:
    def __init__(self, id, street):
        self.id = id
        self.street = street