# pylint: disable= missing-docstring

from typing import List


class Leap:
    @staticmethod
    def leap_check(year: int) -> bool:
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    @staticmethod
    def leap_range(start: int, end: int) -> List[int]:
        years = []
        for year in range(start, end):
            if Leap.leap_check(year):
                years.append(year)
        return years


if __name__ == "__main__":
    # leap = Leap()
    print(Leap.leap_check(year=2020))
