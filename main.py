# pylint: disable= missing-docstring


def is_leap(year: int) -> str:
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_leap(2000))
    print(is_leap(2020))
    print(is_leap(2100))
