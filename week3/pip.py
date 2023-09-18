number = int(input()) # Do not change this line
# Fill in the missing code below
no_7_found_yet = True

# keep dividing it by 10, discarding the remainder, until it becomes 0
while number > 0:
    # remainder = number % 10 == 7
    last_digit = number % 10
    if last_digit == 7:
        no_7_found_yet = False
        break
        
    # discarding the remainder
    number = number // 10 

# at each step checking if the last digit (the discarded remainder) is 7
if no_7_found_yet: # Hint: does this variable name suggest anything? no_7_found_yet
    print("The number does not contain 7.")
else:
    print("The number contains 7.")    

