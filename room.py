class Room:
    
    def __init__(self, color, width, length, position, name, neighbors):
        self.color = color
        self.width = int(width)
        self.length = int(length)
        self.position = position
        self.name = name
        self.neighbors = dict(neighbors)

    