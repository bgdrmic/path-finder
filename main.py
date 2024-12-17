from src import Map

input = """  @---A---+
          |
  x-B-+   C
      |   |
      +---+"""
print(input)
input = [list(row) for row in input.split('\n')]
map = Map(input)
map.traverse_map()
