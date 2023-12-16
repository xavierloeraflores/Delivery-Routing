# Program Solution Overview
## Algorithm Justification
The main core of the algorithm comes in two parts. The first part is the package loading into the trucks and the second part is the delivering of the packages using a greedy algorithm. 

Packages loaded into the trucks in a way that would allow the first truck to delivery high priority packages first. The second truck would then deliver the truck 2 and bundled packages. The third truck would then deliver the delayed or wrong address packages. The remaining packages are distributed between truck 2 and truck 3 since the truck 1 driver needs to return to the hub to drive truck 3. 

The deliver packages part of the algorithm is a greedy algorithm. The algorithm will prioritize packages that have a deadline as its first working set and then move onto packages that don't have a deadline. The algorithm will find the closest package to the current location of the truck and deliver it. The algorithm will then find the next closest package and deliver it. This process will continue until all packages are delivered. The algorithm also takes into account the special package that needs to be delivered last since the delivery address needs to be corrected. 
### Algorithm Strengths
#### Strength 1

#### Strength 2
---

### Algorithm Verification

### Alternative Algorithm Solutions
#### Algorithm 1

#### Algorithm 2

---

## Modifications To The Program Solution

---

## Data Structure Verification
### Alternative Potential Data Structures
#### Data Structure 1

#### Data Structure 2