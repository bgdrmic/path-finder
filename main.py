from src import Map

input = [
    "  @---A---+",
    "          |",
    "  x-B-+   C",
    "      |   |",
    "      +---+",
]

map = Map(input)

path, letters = map.traverse()
print(path)
print(letters)
