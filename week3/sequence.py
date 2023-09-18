# Design an algorithm that generates the first n numbers in the following sequence: 1, 2, 3, 6, 11, 20, 37,
n = int(input())  # Do not change this line


# set variables
t1, t2, t3 = 0, 1, 2
count = 1

while count <= n:
    if count == 1:
        print(1)
    elif count == 2:
        print(2)
    else:
        current_count = t1 + t2 + t3
        print(current_count)
        t1, t2, t3 = t2, t3, current_count

    count += 1
