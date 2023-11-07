from typing import List


def extract_evens(int_list: List[int]) -> List[int]:
    even_list = [item for item in int_list if item % 2 == 0]
    return even_list


def remove_odds(int_list: List[int]) -> None:
    int_list[:] = [item for item in int_list if item % 2 == 0]
