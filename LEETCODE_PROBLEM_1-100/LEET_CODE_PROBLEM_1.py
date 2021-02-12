"""
LEET CODE PROBLEM. 1 : Two Sum

Find two numbers satisfying a condition

condition : target_sum = a + b such as a,b in a given number set.

sample_1 = [2, 7, 11, 15], target_sum = 9
sample_2 = [3, 2, 4] , target_sum = 6
sample_3 = [3, 3] , target_sum = 6
sample_4 = [-3, 0, 3, 32] , target_sum = 0
"""
'''Brute force solution'''
def twoSum(numbers, target_sum):
    # Spatial complexity : O(1)
    # Time complexity : O(n^2)
    for idx, num in enumerate(numbers):
        for idy, other in enumerate(numbers[idx+1:]):
            if num+other == target_sum:
                return [idx, idx+idy+1]
'''One-pass solution'''
def _twoSum(nums: list, target: int) -> list:
    # Spatial complexity : O(n)
    # Time complexity : O(n)
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        print(prevMap)
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return None