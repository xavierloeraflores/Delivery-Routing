# Algorithm Overview

## Stated Problem

The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”

Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for two of the trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

### Assumptions

- Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
- The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
- There are no collisions.
- Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.
- The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.
- There is up to one special note associated with a package.
- The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
- The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.
- The day ends when all 40 packages have been delivered.

## A. Algorithm Overview

Our solution to solve the WGUPS Delivery Routing Problem is to develop a delivery routing program that utilizes a greedy algorithm that uses a nearest neighbor algorithm to find an efficient route and delivery distribution.

## B. Data Structure And Relationship To Components
The package delivery program utilizes a hash table to store the delivery package data and a weighted adjacency matrix, or distance matrix to store the distances between addresses.The hash table data structure contains all the raw package data contained in a package object. The package object contains the package ID, delivery address, deadline, city, zip code, and weight. Alongside the package object, the hash table stores a delivery package object which contains the delivery status, delivery time if delivered, and address object. The distance matrix matrix stores the distances between the addresses. It can look up the distance between two addresses by using the address ID for the row and column index in constant time. The program will update the delivery package object in the hash table after determining which package to deliver first based on the closest address in the distance matrix. 

## C. Overview


## D. Algorithm Justification
The greedy nearest neighbor algorithm is a viable solution to the delivery routing program because it can efficiently find an optimal route and delivery distribution. The nearest neighbor algorithm is a greedy algorithm that finds the shortest path between two points. The nearest neighbor algorithm is a greedy algorithm because it makes the locally optimal choice at each step.

### 1. Algorithm Psuedocode

### 2. Programming Environment

The programming environment features Python version 3.8.9 which is the ninth maintenance release of Python 3.8 released on April 2, 2021.

The programming environment is being ran within MacOS Monterey Version 12.0.1 on a 16 inch MacBook Pro with an Apple M1 Pro processor and 32GB of unified memory.

### 3. Space Time Complexity

**main.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|delivery_routing_system|12| | | 
|load_packages|24| | |
|delivery_algorithm|42| | |
|identify_next_package|52| | |
|interface_loop|79| | |
|main|103| | |



**HashTable.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|Node.__init__|3| | |
|HashTable.__init__|11| | |
|hash_key|19| | |
|insert|24| | |
|update|37| | |
|get|48| | |


**DistanceMatrix.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|read_distance|4| | |
|get_distance_between_addresses|24| | |
|get_closest_address|31| | |


**System.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|create_system|17| | |
|print_system|31| | |


**Truck.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|__init__|20| | |
|load_package|40| | |
|__str__|48| | |
|set_depart_time|54| | |
|attempt_depart|59| | |
|get_undelivered_packages|66| | |
|get_undelivered_packages_addresses|75| | |
|deliver_package|82| | |
|return_to_hub|96| | |
|travel_for_time_in_min|105| | |
|set_address_id|111| | |
|get_priority_packages|115| | |


**DeliveryPackage.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|__init__|24| | |
|print|35| | |
|get_id|60| | |
|set_status_to_delivered|64| | |
|set_status_to_enroute|68| | |
|set_delivered_time|72| | |
|set_truck_id|76| | |

**Package.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |
|read_packages|4| | |
|raw_packages_to_packages|14| | |
|__init__|22| | |
|has_deadline|38| | |
|has_notes|42| | |
|is_delayed|46| | |
|is_truck_2|50| | |
|has_wrong_address|54| | |
|is_bundled|58| | |

**Address.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |


**Utils.py**
| Method | Time Complexity | Space Complexity | Line Number |
| --- | --- | --- | --- |  
|read_addresses|4| | |
|get_address_list|14| | |
|__init__|26| | |
|get_address_by_id|36| | |
|get_address_by_street|45| | |

### 4. Solution scalability & adaptability

### 5. Software Design Efficiency & Maintainability

### 6. Hash Table Strengths & Weaknesses

Strengths:

- Hash tables are very efficient for lookups since they can happen in constant time O(1).
- Hash tables are also very efficient for insertions and deletions since they only need to change to update one array index for each operation as opposed to a linear data structure like an array or linked list which would need to update multiple indexes.
- Hash tables are very flexible and can be used to store any type of data structure.
- Hash tables feature collision resolution which handles the cases for multiple key-values hashing to the same index.

Weaknesses:

- Hash tables can be inefficient when there are a large number of collisions.
- Hash tables do not allow null values
- Hash tables have a limited capacity and will need to be resized or utilize linked nodes if the number of elements exceeds the capacity.
- Hash tables are unordered which do not allow for sorting and make it difficult to retrieve the data in a specific order.

### 7. Key Justification

The delivery routing system will utilize the package's package ID as the key to access the package's data. The package ID is a unique identifier for each package and is a very efficient way to access the package's data from the hash table.

## Resources

I did not use any external sources to complete this writeup.