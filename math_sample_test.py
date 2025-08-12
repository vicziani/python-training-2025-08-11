from math_sample import add


def test_add():
    # Given
    a = 5.0
    b = 6.0
    # When
    result = add(a, b)
    # Then
    assert result == 11.0


def test_add_simple():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 0) == 0


def test_add_float():
    # Ez a számábrázolás pontatlansága miatt van
    assert abs(0.3 - add(0.1, 0.2)) < 1e-9
