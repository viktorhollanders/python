# Here you might want to initialize some variables
UPPER_BOUND = 1000
LOWER_BOUND = 0
number_of_guesses = 10

cmd = input()
guess = 500

print(guess)
# Then start a while loop
while count > 0: 
    print(guess)
    cmd = input()
    if guess == c:
        print("I AM VICTORIOUS")
    elif cmd == "h":
        guess = guess / 2
    elif cmd == "l":
        guess = ((guess / 2 + 1) + (guess - 1)) / 2
    else:
        print("Tsk, tsk, don't try to cheat me")

# These lines you can keep as is



# Now it's up to you to check the command and take appropriate action
# If you detect that the user has not been truthful, you should print the following
