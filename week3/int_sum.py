num = int(input()) # You can copy this line but should not change it
# Fill in the missing code below

total = 0

# while the number is not 10 
while num != 10:
    # if set total to 0
    if num == 10:
        total = 0
        break
    # else number is not 10 add umber to tota l and prompt the user for a new number
    else:
        total += num
        num = int(input()) 

print(total)