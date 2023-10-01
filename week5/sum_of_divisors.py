def sum_of_divisors(number):
    sum_of_divisors = 0

    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    return sum_of_divisors


def decide(number):
    if number == sum_of_divisors(number):
        return f"{number} is a perfect number."
    if number < sum_of_divisors(number):
        return f"{number} is abundant."
    if number > sum_of_divisors(number):
        return f"{number} is deficient."


if __name__ == "__main__":
    input_num = int(input())
    print(decide(input_num))

