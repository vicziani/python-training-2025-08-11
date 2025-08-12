def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a - b


def is_monotonic_increase(numbers: list) -> bool:
    previous = numbers[0]
    for number in numbers:
        if number < previous:
            return False
        previous = number
    return True
