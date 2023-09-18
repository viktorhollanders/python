a_str = input()

# Complete the program below
invers_str = ""

for index in range(len(a_str)):
    if a_str[index] == " ":
        invers_str += a_str[index]
    if a_str[index].isupper():
        invers_str += a_str[index].lower()
    # elif a_str[index].islower():
    else:
        invers_str += a_str[index].upper()

print(invers_str)
