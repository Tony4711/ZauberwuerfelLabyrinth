class Room:

    def __init__(self):
        self.init_rooms()

        
    def init_rooms(self):
        self.rooms = {
            "yellow_room": {
                "width": "6",
                "lentgh": "6",
                "position": "bottom",
                "name": "gelber Raum"
            },
            "white_room": {
                "width": "6",
                "lentgh": "6",
                "position": "top",
                "name": "weißer Raum"
            },
            "green_room": {"width": "6",
                "lentgh": "6",
                "position": "front",
                "name": "grüner Raum"
            },
            "red_room": {
                "width": "6",
                "lentgh": "6",
                "position": "right",
                "name": "roter Raum"
            },
            "blue_room": {
                "width": "6",
                "lentgh": "6",
                "position": "back",
                "name": "blauer Raum"
            },
            "orange_room": {
                "width": "6",
                "lentgh": "6",
                "position": "left",
                "name": "oranger Raum"
            }
        }