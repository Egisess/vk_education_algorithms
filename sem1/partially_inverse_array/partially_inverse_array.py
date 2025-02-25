def inverse_from_to(nums: list, left: int, right: int) -> list:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def solution(nums: list, k: int) -> list:
    if len(nums) == 0:
        return nums

    n = len(nums)
    k = k % n

    inverse_from_to(nums, 0, n - 1)
    inverse_from_to(nums, 0, k - 1)
    inverse_from_to(nums, k, n - 1)

    return nums
