''' 
def find_max_positive_integer():
    max_value = 0
    while True:
        try:
            num = int(input())
            if num < 0:
                break
            if num > max_value:
                max_value = num
        except ValueError:
            print("Please enter a valid integer.")
    return max_value

print("Maximum positive integer entered:", find_max_positive_integer())
'''

# num_int = int(input())  # Do not change this line
# # Fill in the missing code

max_int = 0

while True:
    num_int = int(input())
    if num_int < 0:
        break
    if num_int > max_int:
        max_int = num_int


print(max_int)  # Do not change this line
