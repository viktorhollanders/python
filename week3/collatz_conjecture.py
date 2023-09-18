x = int(input()) # Do not change this line
print(x)
sum = x

while sum > 1:
    if sum % 2 == 0:
        sum /= 2
    else:
        sum = sum * 3 + 1
    print(int(sum))

