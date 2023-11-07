lenght_of_list = int(input())
count = 0
set_of_chores = set()
list_of_chores = []

while count < lenght_of_list:
    user_input = input()

    if user_input not in set_of_chores:
        set_of_chores.add(user_input)
        list_of_chores.append(user_input)

    else:
        pass

    count += 1

print("\n".join(list_of_chores))
