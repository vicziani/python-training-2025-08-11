from math_sample import add, is_monotonic_increase


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


def test_monotonic_increase():
    assert is_monotonic_increase([1, 2, 3, 4, 5])


def test_monotonic_increase_false():
    assert not is_monotonic_increase([1, 2, 3, 2, 5])
