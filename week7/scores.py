def calcualte_scores(sequence: list):
    DECIMAL_POINT = 1
    THREE = 3

    if len(sequence) < THREE:
        return "At least 3 scores needed!"
    else:
        items_sorted = sort_list(sequence)
        remove_first = items_sorted[3:]

        sum_of_scores = 0
        for item in remove_first:
            sum_of_scores += item

        rounded_num = round(sum_of_scores, DECIMAL_POINT)
        return f"Sum of scores (3 lowest removed): {rounded_num}"


def sort_list(a_list: list):
    a_list.sort()
    return a_list


def get_scores(socres):
    score_list = []
    score_split = socres.split(" ")
    for item in score_split:
        score_list.append(float(item))
    return score_list


def main():
    s_input = input()
    scores = get_scores(s_input)
    resault = calcualte_scores(scores)
    print(resault)


if __name__ == "__main__":
    main()
