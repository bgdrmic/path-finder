import pytest

from src import Map, Error, Point
from .test_cases import TEST_CASES, TEST_CASES_WITH_ERRORS


@pytest.fixture
def goonies_map() -> Map:
    return Map(
        [
            "     +-O-N-+",
            "     |     |",
            "     |   +-I-+",
            " @-G-O-+ | | |",
            "     | | +-+ E",
            "     +-+     S",
            "             |",
            "             x",
        ]
    )


@pytest.fixture
def double_intersection_map() -> Map:
    return Map(
        [
            "  x",
            "  C",
            " @--+",
            "+---A",
            "| B",
            "+-+",
        ]
    )


@pytest.fixture
def fork_map() -> Map:
    return Map(
        [
            "        A-B",
            "          |",
            "   @--A---+",
            "          |",
            "     x+   C",
            "      |   |",
            "      +---+",
        ]
    )


def generate_test_ids(test_data):
    return [t[-1] for t in test_data]


@pytest.mark.parametrize(
    "input,expected_output,id",
    TEST_CASES,
    ids=generate_test_ids(TEST_CASES),
)
def test_map_traverse(input, expected_output, id):
    map = Map(input)
    path, letters = map.traverse()
    assert path == expected_output[0]
    assert letters == expected_output[1]


@pytest.mark.parametrize(
    "input,id",
    TEST_CASES_WITH_ERRORS,
    ids=generate_test_ids(TEST_CASES_WITH_ERRORS),
)
def test_map_traverse_with_errors(input, id):
    with pytest.raises(Error):
        map = Map(input)
        map.traverse()


def test_validate_input_throws_error_for_invalid_character():
    input = ["@-a-x"]
    with pytest.raises(Error):
        Map(input)


def test_find_start(goonies_map: Map):
    assert goonies_map.find_start() == Point(3, 1)


def test_location_exists_non_rectangular_map(goonies_map: Map):
    assert goonies_map.location_exists(Point(0, 11)) is True
    assert goonies_map.location_exists(Point(0, 12)) is False
    assert goonies_map.location_exists(Point(2, 12)) is True
    assert goonies_map.location_exists(Point(0, -1)) is False
    assert goonies_map.location_exists(Point(-1, 0)) is False
    assert goonies_map.location_exists(Point(8, 0)) is False


def test_start_map(goonies_map: Map):
    goonies_map.start()
    assert len(goonies_map.visited) == 1
    assert goonies_map.path == "@"
    assert goonies_map.letters == ""
    assert goonies_map.curr_loc == Point(3, 1)
    assert goonies_map.curr_direction is None


def test_move_next(goonies_map: Map):
    goonies_map.start()

    goonies_map.move_next()

    assert len(goonies_map.visited) == 2
    assert goonies_map.path == "@-"
    assert goonies_map.letters == ""
    assert goonies_map.curr_loc == Point(3, 2)
    assert goonies_map.curr_direction == Point(0, 1)


def test_move_next_throws_at_fork(fork_map: Map):
    fork_map.start()

    for _ in range(7):
        fork_map.move_next()

    assert fork_map.curr_loc == Point(2, 10)
    assert fork_map.path[-1] == "+"
    with pytest.raises(Error):
        fork_map.move_next()


def test_can_continue_at_start(goonies_map: Map):
    goonies_map.start()
    assert goonies_map.can_continue() is False


def test_can_continue_through_letter_intersection(goonies_map: Map):
    goonies_map.start()

    for _ in range(4):
        goonies_map.move_next()

    assert goonies_map.curr_loc == Point(3, 5)
    assert goonies_map.curr_direction == Point(0, 1)
    assert goonies_map.can_continue() is True

    for _ in range(8):
        goonies_map.move_next()

    assert goonies_map.curr_loc == Point(3, 5)
    assert goonies_map.curr_direction == Point(-1, 0)
    assert goonies_map.can_continue() is True


def test_can_continue_at_plus(goonies_map: Map):
    goonies_map.start()

    for _ in range(6):
        goonies_map.move_next()

    assert goonies_map.curr_loc == Point(3, 7)
    assert goonies_map.curr_direction == Point(0, 1)
    assert goonies_map.can_continue() is False


def test_can_continue_pass_through_double_intersection(double_intersection_map: Map):
    map = double_intersection_map
    map.start()
    for _ in range(13):
        map.move_next()

    assert map.curr_loc == Point(4, 2)
    assert map.curr_direction == Point(-1, 0)
    assert map.can_continue() is True

    map.move_next()

    assert map.curr_loc == Point(3, 2)
    assert map.curr_direction == Point(-1, 0)
    assert map.can_continue() is True


def test_find_new_direction_at_plus(goonies_map: Map):
    goonies_map.start()

    for _ in range(6):
        goonies_map.move_next()

    assert goonies_map.can_continue() is False
    assert goonies_map.find_new_direction() == Point(1, 0)


def test_find_new_direction_at_letter(double_intersection_map: Map):
    map = double_intersection_map
    map.start()

    for _ in range(4):
        map.move_next()

    assert map.curr_loc == Point(3, 4)
    assert map.can_continue() is False
    assert map.find_new_direction() == Point(0, -1)


def test_find_new_direction_towards_a_letter(double_intersection_map: Map):
    map = double_intersection_map
    map.start()

    for _ in range(3):
        map.move_next()

    assert map.curr_loc == Point(2, 4)
    assert map.can_continue() is False
    assert map.find_new_direction() == Point(1, 0)


def test_find_new_direction_towards_a_letter(double_intersection_map: Map):
    map = double_intersection_map
    map.start()

    for _ in range(3):
        map.move_next()

    assert map.curr_loc == Point(2, 4)
    assert map.can_continue() is False
    assert map.find_new_direction() == Point(1, 0)


def test_find_new_direction_throws_an_error(fork_map: Map):
    fork_map.start()

    for _ in range(7):
        fork_map.move_next()

    assert fork_map.curr_loc == Point(2, 10)
    assert fork_map.can_continue() is False

    with pytest.raises(Error):
        fork_map.find_new_direction()
