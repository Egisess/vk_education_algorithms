def solution_1(nums: list) -> list:
    return nums[::-1]

def solution_2(nums:list) ->list:
    n = len(nums)
    for i in range(n // 2):
        nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
    return nums
