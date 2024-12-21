from typing import Self


class Point:
    def __init__(self, x: int, y: int) -> Self:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self) -> Self:
        return Point(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
