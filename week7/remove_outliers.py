from copy import deepcopy  # In case you need it :)


def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""

    get_min = min(a_list)
    get_max = max(a_list)

    a_list.pop(a_list.index(get_min))

    a_list.pop(a_list.index(get_max))


def without_outliers(a_list: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""

    get_min = min(a_list)
    get_max = max(a_list)

    no_outliers = a_list.copy()
    no_outliers.remove(get_min)
    no_outliers.remove(get_max)

    return no_outliers
