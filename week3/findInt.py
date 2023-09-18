stop_range = int(input())
num_divisor = int(input())

for i in range(10, stop_range):
    # split i in to two and sum up the two digits
    digit_list = list(map(int, str(i)))
    digit_sum = sum(digit_list)
    square_sum = digit_sum**2

    # if the square of sum_digit == i and
    if square_sum == i:
        print(i)


# if the i is devisable with num_divisor and resault is positive
for i in range(1, stop_range):
    divisor_count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            divisor_count += 1

    if divisor_count == num_divisor:
        print(i)
