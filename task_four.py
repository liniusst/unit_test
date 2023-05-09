# pylint: disable= missing-docstring
# write python program that translates integer to roman. Try doing it in TDD style


def int_to_roman(int_value: int) -> str:
    roman_value = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "CX",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    result = ""
    while int_value > 0:
        for key in sorted(roman_value.keys(), reverse=True):
            while int_value >= key:
                result += roman_value[key]
                int_value -= key
    return result


print(int_to_roman(5500))
