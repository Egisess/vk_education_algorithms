def solution_1(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

    return [-1, -1]


print(solution_1([1, 2, 3, 6, 10, 120, 128], 11))
