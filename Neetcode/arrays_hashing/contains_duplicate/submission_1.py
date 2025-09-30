"""
Date: 07/17/2025 16:03
Memory: O(n)
Runtime: O(n)
"""

"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False
"""

def hasDuplicate(nums) -> bool:
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False

print(hasDuplicate([1,2,3,3]))  # True
print(hasDuplicate([1,2,3,4]))  # False