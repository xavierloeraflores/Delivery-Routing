from Utils import CSVReader

# Read the address list from the CSV file
def read_addresses():
    reader = CSVReader("AddressList.csv")
    rows = reader.read()
    addresses = []
    for idx, row in enumerate(rows):
        if idx != 0:
            addresses.append(row)
    return addresses

# Create a list of Address objects from the address list
def get_address_list():
    addresses = read_addresses()
    address_list = []
    idx=1
    for row in addresses:
        address = Address(idx, row[0])
        address_list.append(address)
        idx += 1
    return address_list

# Address class
class Address:
    def __init__(self, id, street):
        self.id = id
        self.street = street

# AddressBook class for looking up addresses
class AddressBook:
    addresses = read_addresses()
    address_list = get_address_list()
        # Get an address object by its id
    @staticmethod
    def get_address_by_id(address_id):
        for address in AddressBook.address_list:
            if address.id == address_id:
                return address
        return None

    # Get an address object by its street
    @staticmethod
    def get_address_by_street( street):
        for address in AddressBook.address_list:
            if address.street == street:
                return address
        return None