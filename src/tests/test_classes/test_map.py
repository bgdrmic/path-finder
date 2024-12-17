import pytest

from src.classes import Map, Error, Point


def test_solution_basic():
    input = [[' ', ' ', '@', '-', '-', '-', 'A', '-', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', 'x', '-', 'B', '-', '+', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@---A---+|C|+---+|+-B-x'
    assert letters == 'ACB'

def test_solution_intersection():
    input = [[' ', ' ', '@'], [' ', ' ', '|', ' ', '+', '-', 'C', '-', '-', '+'], [' ', ' ', 'A', ' ', '|', ' ', ' ', ' ', ' ', '|'], [' ', ' ', '+', '-', '-', '-', 'B', '-', '-', '+'], [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', 'x'], [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', '+', '-', '-', '-', 'D', '-', '-', '+']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@|A+---B--+|+--C-+|-||+---D--+|x'
    assert letters == 'ABCD'
    
def test_solution_letters_in_corners():
    input = [[' ', ' ', '@', '-', '-', '-', 'A', '-', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', 'x', '-', 'B', '-', '+', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', 'C']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@---A---+|||C---+|+-B-x'
    assert letters == 'ACB'

def test_solution_dont_collect_letters_twice():
    input = [[' ', ' ', ' ', ' ', ' ', '+', '-', 'O', '-', 'N', '-', '+'], [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '+', '-', 'I', '-', '+'], [' ', '@', '-', 'G', '-', 'O', '-', '+', ' ', '|', ' ', '|', ' ', '|'], [' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', '+', '-', '+', ' ', 'E'], [' ', ' ', ' ', ' ', ' ', '+', '-', '+', ' ', ' ', ' ', ' ', ' ', 'S'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@-G-O-+|+-+|O||+-O-N-+|I|+-+|+-I-+|ES|x'
    assert letters == 'GOONIES'

def test_solution_compact_turns():
    input = [[' ', '+', '-', 'L', '-', '+'], [' ', '|', ' ', ' ', '+', 'A', '-', '+'], ['@', 'B', '+', ' ', '+', '+', ' ', 'H'], [' ', '+', '+', ' ', ' ', ' ', ' ', 'x']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@B+++B|+-L-+A+++A-+Hx'
    assert letters == 'BLAH'

def test_solution_ignore_after_end_of_path():
    input = [[' ', ' ', '@', '-', 'A', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '+', '-', 'B', '-', '-', 'x', '-', 'C', '-', '-', 'D']]
    map = Map(input)
    path, letters = map.traverse_map()
    assert path == '@-A--+|+-B--x'
    assert letters == 'AB'
    
def test_solution_error_missing_start():
    input = [[' ', ' ', ' ', ' ', ' ', '-', 'A', '-', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', 'x', '-', 'B', '-', '+', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()

def test_solution_error_missing_end():
    input = [[' ', ' ', ' ', '@', '-', '-', 'A', '-', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', 'B', '-', '+', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()

def test_solution_error_multiple_starts():
    input = [[' ', ' ', ' ', '@', '-', '-', 'A', '-', '@', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', 'x', '-', 'B', '-', '+', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()    

def test_solution_error_fork_in_path():
    input = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', '-', 'B'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', '@', '-', '-', 'A', '-', '-', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', 'x', '+', ' ', ' ', ' ', 'C'], [' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()

def test_solution_error_broken_path():
    input = [[' ', ' ', ' ', '@', '-', '-', 'A', '-', '+'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', '-', 'x']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()

def test_solution_error_fork_at_the_start():
    input = [[' ', ' ', 'x', '-', 'B', '-', '@', '-', 'A', '-', 'x']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()

def test_solution_error_fake_turn():
    input = [[' ', ' ', '@', '-', 'A', '-', '+', '-', 'B', '-', 'x']]
    with pytest.raises(Error):
        map = Map(input)
        map.traverse_map()
