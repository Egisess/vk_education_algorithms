def binarySearchSqrt(target: int):
    l = 0
    r = target
    while l <= r:
        mid = (l + r) // 2
        if mid ** 2 > target:
            r = mid - 1
            continue
        elif mid ** 2 < target:
            l = mid + 1
            continue
        return mid
    return l if abs(l ** 2 - target) < abs(r ** 2 - target) else r

if __name__ == '__main__':
    for num in [0, 1, 4, 8, 16, 25, 26]:
        sol = binarySearchSqrt(num)
        print(f'{num}\'s sqrt is {sol}')