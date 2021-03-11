## Parking System In Python

### Run
python -i system.py

```
system.park_vehicle("DL-1244", "BIG")
system.park_vehicle("DL-1245", "SMALL")

system.exit_vehicle("d7557950-36b3-4023-82cd-44cee0d50651")
```

- Parking Lot can have multiple floors
- Floors can have multiple entry exit points
- Spot are filled/vacated based on floors
- It is assumed that the name and distance for all the spots will be unique as per all entry-exit points
- When a vehicle enters the lot, the nearest spot to the entry point is selected using min-heap
- Once a vehicle enters, can only be exited through an entry exit of the same floor.

Scope
- Spots can be distinguished based on sizes, for now the size is only being used to calculate the fare
- The trigger operation when a spot is filled/vacated can be optimized.
- Validation on the registration number of a vehicle
- Test Cases
