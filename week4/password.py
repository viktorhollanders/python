# constants variables for inimum lenght anf maximum lenght of pasword
# constant for the quit command in the program
UPPER_BOUND = 6
LOWER_BOUND = 20
QUIT = "q"

# other variables
pass_count = 0
valid_pass_count = 0
invalid_pass_count = 0

pass_input = input()

while pass_input.lower() != QUIT:
    pass_lenght = len(pass_input)
    if UPPER_BOUND <= pass_lenght <= LOWER_BOUND:
        has_lowercase = False
        has_uppercase = False
        has_number = False

        for char in pass_input:
            # Checks assci code
            ascci_code = ord(char)

            if 48 <= ascci_code <= 57:
                has_number = True
            if 65 <= ascci_code <= 90:
                has_uppercase = True
            if 97 <= ascci_code <= 122:
                has_lowercase = True

        if has_number and has_uppercase and has_lowercase:
            pass_count += 1
            valid_pass_count += 1

            print(f"{pass_input}: Valid password of length {pass_lenght}.")
        else:
            pass_count += 1
            invalid_pass_count += 1

            if not has_lowercase:
                print(f"{pass_input}: Missing lower case letter.")
            if not has_uppercase:
                print(f"{pass_input}: Missing upper case letter.")
            if not has_number:
                print(f"{pass_input}: Missing numeric letter.")

    else:
        pass_count += 1
        invalid_pass_count += 1

        print(f"{pass_input}: Invalid length.")
    pass_input = input()
print(
    f"You tried {pass_count} passwords, {valid_pass_count} valid, {invalid_pass_count} invalid."
)
