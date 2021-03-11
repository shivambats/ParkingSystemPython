import json

from models.entry_exit import EntryExit
from models.floor import Floor
from models.parking_lot import ParkingLot

import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

with open("data.json", "r") as f:
    data = json.load(f)
    floors = list()
    entry_exit = list()
    spots = list()
    for floor in data["floor"]:
        entry_exit = list()
        for entryexit in floor["entries"]:
            spots = list()
            entry_exit.append(EntryExit(id=entryexit["id"], spots=entryexit["spots"]))
        floors.append(Floor(floor["id"], entry_exit=entry_exit))
    parking_lot_obj = ParkingLot(floors)
