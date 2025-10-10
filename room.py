class Room:
    
    def __init__(self, color, width, length, position, name, neighbors):
        self.color = color
<<<<<<< HEAD
        self.width = width
        self.lenght = length
        self.postion = position
        self.name = name
        self.neighbor = neighbors
=======
        self.width = int(width)
        self.length = int(length)
        self.position = position
        self.name = name
        self.neighbors = dict(neighbors)
>>>>>>> main

    