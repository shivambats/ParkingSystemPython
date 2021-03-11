from models.floor import Floor
from typing import List


class ParkingLot:
    """
    ParkingLot class is
    """
    def __init__(self, floors: List[Floor]):
        self.floors = floors
        self.ticket_map = dict()
