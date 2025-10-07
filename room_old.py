class Room:

    def __init__(self):
        self.init_rooms()


    def init_rooms(self):

        self.rooms = {
            "yellow_room": Room(
                color = "yellow",
                width = 6,   
                length = 6,
                position = "bottom",
                name = "gelber Raum",
                neighbors = {
                    "north": "green_room",
                    "east": "red_room",
                    "south": "blue_room",
                    "west": "orange_room",
                }
            ),
            "white_room": Room(
                color = "white",
                width = 6,
                length = 6,
                position = "top",
                name = "weißer Raum",
                neighbors = {
                    "north": "blue_room",
                    "east": "red_room",
                    "south": "green_room",
                    "west": "orange_room",
                }
            ),
            "green_room": Room(
                color = "green",
                width = 6,
                length = 6,
                position = "front",
                name = "grüner Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "red_room",
                    "south": "yellow_room",
                    "west": "orange_room",
                }
            ),
            "red_room": Room(
                color = "red",
                width = 6,
                length = 6,
                position = "right",
                name = "roter Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "blue_room",
                    "south": "yellow_room",
                    "west": "green_room",
                }
            ),
            "blue_room": Room(
                color = "blue",
                width = 6,
                length = 6,
                position = "back",
                name = "blauer Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "orange_room",
                    "south": "yellow_room",
                    "west": "red_room",
                }
            ),
            "orange_room": Room(
                color = "orange",
                width = 6,
                length = 6,
                position = "left",
                name = "oranger Raum",
                neighbors = {
                    "north": "white_room",
                    "east": "green_room",
                    "south": "yellow_room",
                    "west": "blue_room",
                }
            )
        }