def twoSum(nums:list, target:int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[target - num] = (i, num)

    for i, num in enumerate(nums):
        if num in hashmap and hashmap[num][0] != i:
            return [num, hashmap[num][1]]
    return []
        
if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    target = 8
    res = twoSum(nums, target)
    print(f'nums = {nums}, target = {target}: res = {res}')

    nums = [1, 2, 3, 4, 4]
    target = 8
    res = twoSum(nums, target)
    print(f'nums = {nums}, target = {target}: res = {res}')