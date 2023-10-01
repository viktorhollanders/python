import math

QUIT = "q"
COLLECT = "c"
INVERSE = "i"
HEX_NUMBER = "h"


def collect_digits(a_str: str) -> int:
    digits = ""

    for char in a_str:
        if char.isdigit():
            digits += char

    if digits:
        return int(digits)
    else:
        return ""


def inverse_case(a_str: str) -> str:
    inversed_str = ""

    for char in a_str:
        if char == " ":
            inversed_str += char
        elif char.isupper():
            inversed_str += char.lower()
        else:
            inversed_str += char.upper()
    return inversed_str


def to_hex(an_int):
    HEX_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F",]

    quotient = int(an_int)
    hex_output = ""

    while quotient > 0:
        remainder = quotient % 16
        hex_output = HEX_NUMBERS[remainder] + hex_output
        quotient = quotient // 16

    return hex_output


user_input = input()
output = ""

while user_input != QUIT:
    if user_input == "c":
        collect_input = input()
        print(collect_digits(collect_input))
    elif user_input == "i":
        inverse_input = input()
        print(inverse_case(inverse_input))
    elif user_input == "h":
        hex_input = input()
        print(to_hex(hex_input))

    user_input = input()


# ord draga hex frá 