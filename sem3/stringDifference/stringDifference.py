def stringDifference(str1: str, str2:str) -> str:
    res = 0
    str1 = list(str1)
    str2 = list(str2)
    for s in str1:
        res ^= ord(s)
    for s in str2:
        res ^= ord(s)
    return chr(res)

if __name__ == '__main__':
    a = 'uio'
    b = 'oeiu'
    res = stringDifference(a, b)
    print(f'a = {a}, b = {b}: difference is {res}')