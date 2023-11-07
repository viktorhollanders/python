def list_to_int_tuple(search_list):
    list_of_ints = []
    for item in search_list:
        try:
            list_of_ints.append(int(item))
        except:
            pass

    return tuple(list_of_ints)
