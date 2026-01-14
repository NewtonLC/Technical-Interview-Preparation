# Date: 01/13/2026 16:54
# Memory: O(1)
# Runtime: O(n^2)

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        def bestJump(position, maxJump):
            best = 0
            best_jump = position
            for i in range(1,maxJump+1):
                if best < i + nums[position+i]:
                    best = i + nums[position+i]
                    best_jump = position + i
            return best_jump

        position = 0
        while nums[position] != 0:
            if position + nums[position] >= len(nums)-1:
                return True
            position = bestJump(position, nums[position])

        return False
    
    # This problem is better to iterate backwards, that way you only care about one solution that works rather than trying out a bunch of potential solutions that might all work.
"""

def canJump(nums):
    if len(nums) == 1:
        return True
    
    def bestJump(position, maxJump):
        best = 0
        best_jump = position
        for i in range(1,maxJump+1):
            if best < i + nums[position+i]:
                best = i + nums[position+i]
                best_jump = position + i
        return best_jump

    position = 0
    while nums[position] != 0:
        if position + nums[position] >= len(nums)-1:
            return True
        position = bestJump(position, nums[position])

    return False

# Test cases
print(canJump([2,3,1,1,4]))  # True
print(canJump([3,2,1,0,4]))  # False