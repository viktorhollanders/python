def main():
    grade_dictionary = {}

    add_grade(grade_dictionary)
    while prompt_for_more():
        add_grade(grade_dictionary)

    display_grades(grade_dictionary)


def prompt_for_more() -> bool:
    """Checks if the user wants to add more grades."""
    aks_to_add = input().lower()

    if aks_to_add == "y":
        return True
    return False


def add_grade(dictionary: dict) -> None:
    email = input()
    grade = int(input())

    if email in dictionary:
        dictionary[email].append(grade)
    else:
        dictionary[email] = [grade]


def display_grades(dictionary: dict) -> None:
    sorted_emails = []

    for email in dictionary:
        sorted_emails.append(email)
    
    sorted_emails.sort()

    for email in sorted_emails:
        avrage = calc_avrage(dictionary[email])
        print(f"{email}: {avrage:.2f}")


def calc_avrage(grades: list[int]) -> float:
    return sum(grades) / len(grades)


if __name__ == "__main__":
    main()
