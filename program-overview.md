# Program Solution Overview

## Algorithm Justification

The main core of the algorithm comes in two parts. The first part is the package loading into the trucks and the second part is the delivering of the packages using a nearest neighbor greedy algorithm.

Packages loaded into the trucks in a way that would allow the first truck to delivery high priority packages first. The second truck would then deliver the truck 2 and bundled packages. The third truck would then deliver the delayed or wrong address packages. The remaining packages are distributed between truck 2 and truck 3 since the truck 1 driver needs to return to the hub to drive truck 3.

The deliver packages part of the algorithm is a greedy algorithm. The algorithm will prioritize packages that have a deadline as its first working set and then move onto packages that don't have a deadline. The algorithm will find the closest package to the current location of the truck and deliver it. The algorithm will then find the next closest package and deliver it. This process will continue until all packages are delivered. The algorithm also takes into account the special package that needs to be delivered last since the delivery address needs to be corrected.

### Algorithm Strengths

#### Strength 1

Greedy algorithms are simple to implement and understand. They make locally optimal choices that can create a result that is sufficiently efficient. The delivery routing program uses a greedy algorithm that optimizes for loading the priority packages across all trucks to be delivered on time and then for finding the next closest package and then delivering it.

#### Strength 2

Greedy algorithms are great for finding a suitable solution quickly rather than spending resources finding the best most optimal solution. The delivery routing program uses a nearest greedy algorithm that optimizes for finding the next closest package and then delivering it rather than finding the quickest route to deliver all packages considering all possible routes.

---

### Algorithm Verification

The algorithm was verified by running the program and checking the results against the requirements of the project. For each package, the program returns the delivery status, time if the package has been delivered, address, deadline, city, zip code, and weight. It also returns information about each truck including load, mileage, and return time if the truck has returned. The program was finally verified by running the program and checking the results against the CSV files.

### Alternative Algorithm Solutions

#### Alternative Algorithm 1

The A\* algorithm would be an excellent alternative to the greedy algorithm we used in our program. The A\* algorithm is a path finding algorithm that uses a heuristic to find the best path to a goal. The A\* algorithm differs from our greedy algorithm since its goal is to find the best path to deliver all packages.

#### Alternative Algorithm 2

Utilizing simulated annealing would be another alternative to the greedy algorithm we used in our program. Simulated annealing approximates the global optimum of a given function to find the best path by generating random potential solutions and then either accepting or rejecting. The simulated annealing algorithm differs from our greedy algorithm since its goal is to find the best path to deliver all packages.

---

## Modifications To The Program Solution

---

## Data Structure Verification

### Alternative Potential Data Structures

#### Data Structure 1

#### Data Structure 2
