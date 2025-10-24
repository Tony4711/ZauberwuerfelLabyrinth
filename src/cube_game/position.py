from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy 