from CSVReader import CSVReader

def read_distances():
    reader = CSVReader("DistanceTable.csv")
    rows = reader.read()
    distances = []
    for row in rows:
        distances.append(row)
    return distances

def get_distance_between_addresses(address1_id, address2_id, distances):
    if (address2_id> address1_id):
        return distances[address2_id][address1_id]
    return distances[address1_id][address2_id]