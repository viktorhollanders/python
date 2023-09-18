def generate_sequence(n):
    if n == 1:
        return [1]

    a, b = 1, 1
    sequence = [1]

    for i in range(2, n + 1):
        next_num = sequence[-1] + a
        sequence.append(next_num)
        a, b = b, a + b + 1

    return sequence


n = int(input())  # Do not change this line
result = generate_sequence(n)
for num in result:
    print(num)
