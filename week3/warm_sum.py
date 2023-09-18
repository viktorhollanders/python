# Here's something to get you going
# (you might need to add indentation or move it around):
answer = input("You need something doubled? (Y)es? \n")


while True:
    # if answer is not yes quit the program
    if answer != 'Y':
        break
    # else prompt for a number and print it times 2 with 6 extra digits
    # then prompt user again
    else:
        number = float(input("All right, then. Give me a number, and I'll double it for ya: \n"))
        print(format(number * 2, '.6f'))
        answer = input("You need something else doubled? (Y)es? ")
        