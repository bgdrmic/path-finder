from src.classes import Point


def test_equals():
    p1 = Point(2, 2)
    p2 = Point(2, 2)
    p3 = Point(2, 3)
    p4 = Point(3, 2)

    assert p1 == p2
    assert p3 != p1
    assert p4 != p1
    assert p1 != (2, 2)

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
    p = Point(1, 1)
    t = (1, 1)
    
    assert hash(p) == hash(t)