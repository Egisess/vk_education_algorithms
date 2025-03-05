from collections import deque


def is_palindrome(string):
    dq = deque()
    string = string.lower()

    dq.extend(string)

    for s in string:
        if s != dq.pop():
            return False

    return True


def is_palindrome_2(string):
    string = string.lower()
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome_2('Aa'))
