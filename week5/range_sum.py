def sum_of_range(start, end, step):
    int_sum = 0

    for i in range(start, end + 1, step):
        int_sum += i
    return int_sum


if __name__ == "__main__":
    start = int(input())
    end = int(input())
    step = int(input())

    print(sum_of_range(start, end, step))
