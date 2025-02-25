def merge_sorted_arrays(array_first, array_second):
    first, second = 0, 0
    res = []

    while first < len(array_first) and second < len(array_second):
        if     array_first[first] <=  array_second[second]:
            res.append(array_first[first])
            first += 1
        else:
            res.append(array_second[second])
            second += 1

    res.extend(array_first[first:])
    res.extend(array_second[second:])

    return res

# Не совсем понял почему второе решение в семинаре прописано как без доп аллокаций памяти
# если мы по сути экономим только аллокацию первого массива (второй массив дублируется нулями)
# а соответственно пространственная сложность такая же
