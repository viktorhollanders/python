# extract_first_number_from_string definition goes here


def extract_first_number_from_string(string_to_search: str) -> int:
    first_number = ""
    has_seen_num = False

    for char in string_to_search:
        if char.isdigit():
            first_number += char
            has_seen_num = True
        elif has_seen_num:
            break

    if has_seen_num:
        return int(first_number)
    
    return -1


if __name__ == "__main__":
    string = input()
    print(extract_first_number_from_string(string))
