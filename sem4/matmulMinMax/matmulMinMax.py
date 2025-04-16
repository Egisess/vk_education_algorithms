from sem4.treeRestore import treeRestore

def matmulMinMax(nums: list):
    if len(nums) < 3:
        return -1
    
    min_index = 1
    max_index = 2
    i = 1
    while i < len(nums):
        min_index = i
        i = 2 * i + 1
    
    while i < len(nums):
        max_index = i
        i = 2 * i + 2
    
    result = nums[min_index] * nums[max_index]