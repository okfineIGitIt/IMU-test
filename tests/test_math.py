from src import cube


def test_point_rotation():
    x, y = cube.rotate_point_around_origin(0, 0, 0, 1, 90)
    assert x == 1
    assert y == 0
