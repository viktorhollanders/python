def main():
    num1_str = input()
    num2_str = input()

    result = divide_safe(num1_str, num2_str)
    print(result)


def divide_safe(num1: str, num2: str):
    """Returns num1/num2 if the input is valid, else None."""

    try:
        return round(float(num1) / float(num2), 5)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    main()
