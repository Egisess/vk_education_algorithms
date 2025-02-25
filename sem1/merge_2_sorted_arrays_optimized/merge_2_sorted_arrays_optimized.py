def merge_sorted_arrays(array_first, array_second):
    first, second = len(array_first) - len(array_second) - 1, len(array_second) - 1
    third = len(array_first) - 1

    while third >= 0:
        if second < 0 or (array_first[first] >= array_second[second] and first >= 0):
            array_first[third] = array_first[first]
            first -= 1
        elif first < 0 or (array_first[first] < array_second[second] and second >= 0):
            array_first[third] = array_second[second]
            second -= 1
        third -= 1
    return array_first

