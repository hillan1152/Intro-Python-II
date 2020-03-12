# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        room_string = "------------"
        room_string += "\n\n"
        room_string += f"You are in: {self.name}"
        room_string += "\n\n"
        room_string += f"{self.description}"
        room_string += "\n\n"
        room_string += f"{self.get_exits()}"
        return room_string

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return exits
        # Assign attributes to a class
