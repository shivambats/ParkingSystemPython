from typing import List
import heapq
from models.spot import Spot


class EntryExit:
    def __init__(self, id, spots: List):
        self.id = id
        self.spots = spots
        self.distance_spot_map = dict()
        self.heaped_spot = list()
        self.initialize_heap(self.spots)

    def initialize_heap(self, spots):
        """
        Initializes heap and maintains the parking spots in the order of distance from the corresponding entry-exit point

        :param spots: dictionary of spots
        :return:
        """
        self.heaped_spot = list()
        for each in spots:
            self.distance_spot_map[each["distance"]] = Spot(each["name"], each["size"])
            if each["vacant"]:
                self.heaped_spot.append(each["distance"])
        heapq.heapify(self.heaped_spot)

    def get_nearest_parking(self):
        """
        Gets the nearest parking spot from the entry point

        :return:
        """
        try:
            return self.distance_spot_map[heapq.heappop(self.heaped_spot)]
        except IndexError as err:
            return None

    def spot_fill_other_entry_trigger(self, name):
        """
        Trigger once the spot is filled in the floor,
        Updates the spots data for the object and re initializes the heap

        :param name:
        :return:
        """
        for each in self.spots:
            if each["name"] == name:
                each["vacant"] = False
        self.initialize_heap(self.spots)

    def spot_vacant_trigger(self, name):
        """
        Trigger once a spot is vacated in the floor,
        Updates the spots data for the object and re initializes the heap

        :param name:
        :return:
        """
        for each in self.spots:
            if each["name"] == name:
                each["vacant"] = True
        self.initialize_heap(self.spots)

    def __str__(self):
        return self.id

    def __repr__(self):
        return str(self.id)
