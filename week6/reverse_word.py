def main():
    file_name = input()

    reverse_word(file_name)


def reverse_word(file_name):
    for line in open_file(file_name):
        # clean up the input string
        clean_line = line.strip()
        reverse_line(clean_line)


def open_file(file):
    return open(file)


def reverse_line(line):
    output = ""
    line_split = line.split(" ")

    for word in line_split:
        if not line_split[-1]:
            output += word[::-1]
        else:
            output += f"{word[::-1]} "

    print(output)


if __name__ == "__main__":
    main()
