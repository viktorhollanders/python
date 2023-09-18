# take input
n = int(input())

sum_of_fractions = 0

for i in range(n):
    denomenator = 2 ** (i + 1)
    fraction = 1 / denomenator
    sum_of_fractions += fraction
    print(sum_of_fractions)
