import re

from .point import Point
from .error import Error

all_directions = [Point(1, 0), Point(-1, 0), Point(0, 1), Point(0, -1)]


class Map:
    def __init__(self, input: list[str]):
        self.map = [list(row) for row in input]
        self.curr_loc: Point | None = None
        self.curr_direction: Point | None = None
        self.path: str = ""
        self.letters: str = ""
        self.visited: set[Point] = set()

        self.validate_input(input)

    def validate_input(self, input: list[str]):
        input_str = "".join(input)

        if re.search(r"[^A-Z\-|+x@ ]", input_str):
            raise Error("Invalid character in the input")

        if input_str.count("@") != 1 or input_str.count("x") != 1:
            raise Error("Wrong number of ending or starting points")

    def find_start(self) -> Point:
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if char == "@":
                    return Point(i, j)

        raise Error("No starting points")  # this should be impossible to reach

    def start(self):
        self.curr_loc = self.find_start()
        self.visited = {self.curr_loc}
        self.path += "@"
        self.curr_direction = None

    def location_exists(self, loc: Point) -> bool:
        return (
            loc.x >= 0
            and loc.x < len(self.map)
            and loc.y >= 0
            and loc.y < len(self.map[loc.x])
        )

    def find_new_direction(self) -> Point:
        possible_directions = []
        for direction in all_directions:
            if self.curr_direction and direction == -self.curr_direction:
                continue
            if self.path[-1] == "+" and direction == self.curr_direction:
                continue

            new_loc: Point = self.curr_loc + direction
            if not self.location_exists(new_loc):
                continue

            char = self.map[new_loc.x][new_loc.y]
            if (
                char == " "
                or char == "@"
                or (direction.x == 0 and char == "|")
                or (direction.y == 0 and char == "-")
            ):
                continue

            possible_directions.append(direction)

        if len(possible_directions) > 1:
            raise Error("Fork in the path")
        elif len(possible_directions) == 0:
            raise Error("Path ended abruptly")

        return possible_directions[0]

    def can_continue(self) -> bool:
        if self.curr_direction is None or self.path[-1] == "+":
            return False

        new_loc: Point = self.curr_loc + self.curr_direction
        if not self.location_exists(new_loc):
            return False

        new_char = self.map[new_loc.x][new_loc.y]

        return (
            new_char != " "
            and new_char != "@"
            and (
                new_loc in self.visited
                or (self.curr_direction.x == 0 and new_char != "|")
                or (self.curr_direction.y == 0 and new_char != "-")
            )
        )

    def move_next(self):
        if self.curr_direction is not None and self.can_continue():
            new_direction = self.curr_direction
        else:
            new_direction = self.find_new_direction()

        new_loc: Point = self.curr_loc + new_direction
        new_char = self.map[new_loc.x][new_loc.y]

        self.path += new_char
        if re.search(r"[A-Z]", new_char) is not None and new_loc not in self.visited:
            self.letters += new_char

        self.visited.add(new_loc)
        self.curr_direction = new_direction
        self.curr_loc = new_loc

        return new_char

    def traverse(self) -> tuple[str, str]:
        self.start()
        last_char = self.path[0]

        while last_char != "x":
            last_char = self.move_next()

        return self.path, self.letters
