def main():
    name = get_name()
    if name:
        age = get_age()

    print(f"Nice to meet you {name}. Congratulations on your {age} years.")


def get_name() -> str:
    while True:
        user_input = input("What's your name? ")

        if user_input == "":
            print("Please enter a valid name.")
        elif any(char.isdigit() for char in user_input):
            print("Please enter a valid name.")
        else:
            return user_input


def get_age() -> str:
    while True:
        try: 
            user_input = int(input("How old are you? "))
            if  user_input  < 0 or user_input > 127:
                print(f"You seriously expect me to believe you are {user_input} years old?")
            else:
                return user_input
        
        except ValueError:
            print("Please enter an integer.")
            


if __name__ == "__main__":
    main()
