def solution(nums: list) -> list:
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[right] == 0 and nums[left] == 1:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
        elif nums[left] == 0:
            left += 1
        elif nums[right] == 1:
            right -= 1
