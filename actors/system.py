"""
System module to manage the vehicles coming in and out of an entry-exit point
"""

from big_car import BigCar
from models.entry_exit import EntryExit
from models.floor import Floor
from data_init import parking_lot_obj as parking_lot
from small_car import SmallCar
from uuid import uuid4


class System:
    def __init__(self, floor: Floor, entry_exit: EntryExit):
        self.floor = floor
        self.entry_exit = entry_exit

    def park_vehicle(self, registration_number, size):
        """
        The function parks the vehicle by assigning it a spot from the entry-exit point it has entered from, it also
        assumes the size of the vehicle to be judged before and is passed as an argument. Once parked, returns a
        random ticket id which is then used to calculate the fare while exiting the parking lot

        :param registration_number: Registration number of the vehicle
        :param size: Size of the vehicle, Can be either BIG or SMALL
        :return: TicketId Str
        """
        nearest_spot = self.entry_exit.get_nearest_parking()
        if not nearest_spot:
            print("No Spot vacant")
            return
        self.floor.fill_trigger_other_entry_exit(self.entry_exit, str(nearest_spot))
        ticket = uuid4()
        if size == "BIG":
            parking_lot.ticket_map[str(ticket)] = BigCar(registration_number, str(nearest_spot))
        else:
            parking_lot.ticket_map[str(ticket)] = SmallCar(registration_number, str(nearest_spot))
        print(f"Car with ticket id {ticket} is parked")

    def exit_vehicle(self, ticket_id):
        """
        Expects a ticketid which is then searched in the parking lot ticket map and returns the fare and Car information
        :param ticket_id:
        :return:
        """
        try:
            car = parking_lot.ticket_map[ticket_id]
        except KeyError as err:
            print("Invalid Ticket id")
        else:
            fare = car.getFare()
            print(f"Payment of {fare} is cleared")
            self.floor.vacant_trigger_other_entry_exit(car.spot)


s = System(parking_lot.floors[0], parking_lot.floors[0].entry_exit[0])
