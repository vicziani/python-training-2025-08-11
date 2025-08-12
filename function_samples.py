def signum(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def absolute_value(x: int) -> int:
    # if x < 0:
    #     return -x
    # else:
    #     return x
    return signum(x) * x


def rectangle_area(length: float, width: float) -> float:
    return length * width


def rectangle_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)


def circle_area(radius: float) -> float:
    return 3.14 * (radius**2)


def circle_circumference(radius: float) -> float:
    return 2 * 3.14 * radius


def max(a: int, b: int) -> int:
    return a if a > b else b


if __name__ == "__main__":
    print("SAMPLES")
    print(signum(10))
    print(signum(-10))
