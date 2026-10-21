from numbers import Real


def add(a: Real, b: Real) -> Real:
    """Додає два дійсні числа; рядки та bool не є коректним вводом."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Аргументи мають бути числами, не bool")
    if not isinstance(a, Real) or not isinstance(b, Real):
        raise TypeError("Аргументи мають бути дійсними числами")
    return a + b


if __name__ == "__main__":
    print("Result:", add(2, 3))
