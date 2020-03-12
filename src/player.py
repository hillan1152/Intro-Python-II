# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print(
                f"Cannot Go That Way \n You remain in {self.current_room.name} \n Choose another direction")
# getattr
# MVC
# Model, View, Controller all layers
# THIS PLAYER.PY IS A MODEL LAYER
# Fat models, skinny controllers
# adv.py is a control layer.
# define as many objects in the classes as possible.
# don't want to mix all our prints with controller either.
