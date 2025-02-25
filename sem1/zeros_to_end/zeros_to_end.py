def zeros_to_end(nums: list) -> None:
    left, right = 0, 0

    while right < len(nums):
        if nums[left] != 0:
            left += 1
            right += 1
        elif nums[left] == 0 and nums[right] == 0:
            right += 1
        elif nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
