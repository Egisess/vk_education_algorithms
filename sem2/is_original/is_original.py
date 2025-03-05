from collections import deque


def is_original(A, B):
    dq = deque()
    for val in A:
        dq.append(val)

    for val in B:
        if dq and dq[0] == val:
            dq.popleft()
    return len(dq) == 0


def is_original_2(A, B):
    left = 0
    right = 0
    while right < len(B) and left < len(A):
        if B[right] == A[left]:
            left += 1
        right += 1
    return left == len(A)

# Прbvth чтобы сломать третий вариант [1,2,3],[3,2,1]