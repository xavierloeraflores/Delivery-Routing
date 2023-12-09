from Utils import CSVReader

# Read the distance table from the CSV file
def read_distances():
    reader = CSVReader("DistanceTable.csv")
    rows = reader.read()
    distances = []
    for row in rows:
        new_row = []
        for cell in row:
            try:
                cell = float(cell)
            except ValueError:
                cell = -1.0
            new_row.append(cell)
        distances.append(new_row)
    return distances

# Get the distance between two addresses
def get_distance_between_addresses(address1_id, address2_id, distances):
    if (address2_id> address1_id):
        return distances[address2_id][address1_id]
    return distances[address1_id][address2_id]

# Get the closest address to the start address
def get_closest_address(start_address_id, address_ids, distances):
    shortest_distance = 100000000.0
    shortest_address_id = 0
    for cur_address_id in address_ids:
        if cur_address_id != start_address_id:
            cur_distance = get_distance_between_addresses(start_address_id, cur_address_id, distances)
            if cur_distance < shortest_distance:
                shortest_distance = cur_distance
                shortest_address_id = cur_address_id
    return shortest_address_id