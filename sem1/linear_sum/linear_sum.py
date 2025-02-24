def solution_1(n: int) -> int:
    return int(n * (n + 1) / 2)


def solution_2(n: int) -> int:
    res = 0
    left, right = 1, n

    while left < right:
        res += left + right
        left += 1
        right -= 1

    if left == right:
        res += right

    return res


