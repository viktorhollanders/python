import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = get_suffix()

    # TODO: Finish the program
    count = 0

    for line in open_file():
        # cleans up the input line
        clean_line = line.strip("\n")

        # check if word ends with a suffix
        if clean_line.endswith(country_suffix):
            count += 1
            print(clean_line)
    print(f"{count} countries with suffix {country_suffix} in total.")


def get_suffix():
    # You can use stderr to display output in command line but not on Gradescope.
    sys.stderr.write(INPUT_PROMPT)
    return input()


def open_file():
    return open(COUNTRIES_OF_THE_WORLD)


if __name__ == "__main__":
    main()
