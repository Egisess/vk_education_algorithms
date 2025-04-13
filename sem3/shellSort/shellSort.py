def shellSort(array):
    res = [i for i in array]
    n = len(res)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = res[i]
            j = i
            while j >= interval and res[j - interval] > temp:
                res[j] = res[j - interval]
                j -= interval

            res[j] = temp
        interval //= 2
    return res

if __name__ == '__main__':
    nums = [0, -1, 10, 2, 15, 44]
    res = shellSort(nums)
    print(f'nums = {nums}, res = {res}')