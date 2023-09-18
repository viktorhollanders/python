a_str = input()
char_to_count = input()

for index in range(len(a_str)):
    if a_str[index] == char_to_count:
        print(index)
