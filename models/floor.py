from typing import List

from models.entry_exit import EntryExit


class Floor:
    def __init__(self, id, entry_exit: List[EntryExit]):
        self.id = id
        self.entry_exit = entry_exit

    def vacant_trigger_other_entry_exit(self, name):
        """
        Sends trigger to all the other entry exit points once a vehicle vacates the parking lot

        :param name: Name of the spot vacated
        :return:
        """
        for entry_exit_point in self.entry_exit:
            entry_exit_point.spot_vacant_trigger(name)

    def fill_trigger_other_entry_exit(self, entry_obj, name):
        """
        Sends trigger to all the other entry exit points once a vehicle enters the parking lot so the spots can be removed
        from the vacated spots for all other entry points

        :param entry_obj: The entry point object from where the car has entered the parking lot
        :param name:
        :return:
        """
        for entry_exit_point in self.entry_exit:
            if entry_exit_point != entry_obj:
                entry_exit_point.spot_fill_other_entry_trigger(name)

    def __str__(self):
        return self.id

    def __repr__(self):
        return str(self.id)
