def subtract_lists(list1, list2):
    result = list1.copy()
    for item in list2:
        if item in result:
            result.remove(item)
    return result