from typing import List, Tuple


def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """

    data_type_list = []
    boolean_tuple = ()
    for item in a_list:
        try:
            to_int = int(item)
            data_type_list.append(to_int)
        except:
            data_type_list.append(item)

    for item in data_type_list:
        bool_item = bool(item)
        boolean_tuple += (bool_item,)

    return boolean_tuple

