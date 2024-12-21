from src import Point


def test_equals():
    p1 = Point(2, 2)
    p2 = Point(2, 2)
    p3 = Point(2, 3)
    p4 = Point(3, 2)
    t = (2, 2)

    assert p1 == p2
    assert p3 != p1
    assert p4 != p1
    assert p1 != t


def test_add():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    p3 = Point(4, 6)

    assert p3 == p1 + p2


def test_negative():
    p1 = Point(1, 2)
    p2 = Point(-1, -2)

    assert p2 == -p1


def test_hash():
    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(2, 1)
    t1 = (1, 1)
    t2 = (2, 2)

    assert hash(p1) == hash(t1)
    assert hash(p1) != hash(t2)
    assert hash(p1) == hash(p2)
    assert hash(p1) != hash(p3)
