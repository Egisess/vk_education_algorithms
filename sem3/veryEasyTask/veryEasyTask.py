def veryEasyTask(x: float, y: float, target:int) -> float:
    l = 0
    r = (target - 1) * max(x, y) # Максимальная граница времени

    while l + 1 < r:
        mid = (l + r) // 2
        if mid // x + mid // y < target - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)

if __name__ == '__main__':
    for x, y, target in [(1, 2, 1), (1, 10, 9), (5, 10, 4)]:
        res = veryEasyTask(x, y, target)
        print(f'x = {x}, y = {y}, target = {target}: {res}')