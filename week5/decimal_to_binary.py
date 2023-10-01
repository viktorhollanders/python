import math


def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""

    # Fill in the missing code
    if decimal == 0:
        return "0"

    binary = ""
    quotient = decimal

    while quotient > 0:
        if quotient % 2 == 0:
            binary += "0"
            quotient = math.floor(quotient / 2)
        else:
            binary += "1"
            quotient = math.floor(quotient / 2)

    return binary[::-1]


if __name__ == "__main__":
    deci = int(input())
    print(decimal_to_binary(deci))
