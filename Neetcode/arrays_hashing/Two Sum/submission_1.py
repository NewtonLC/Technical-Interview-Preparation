"""
Date: 07/17/2025 16:32
Memory: O(n)
Runtime: O(n)
"""

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in nums_hash:
                return [nums_hash[difference], i]
            nums_hash[nums[i]] = i

        return
"""

def twoSum(nums, target):
    nums_hash = {}

    for i in range(len(nums)):
        difference = target-nums[i]
        if difference in nums_hash:
            return [nums_hash[difference], i]
        nums_hash[nums[i]] = i

    return

print(twoSum([1,2,3,4], 6))  # [1, 2]
print(twoSum([1,2,3,4], 8))  # None