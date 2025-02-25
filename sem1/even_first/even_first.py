def even_first(nums: list) -> None:
    n = len(nums)
    left, right = 0, 0

    while right < n:
        if nums[left] % 2 == 0:
            left += 1
            right += 1
        elif nums[right] % 2 == 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        elif nums[left] % 2 == 1:
            right += 1
