# Date: 01/30/2026 14:18
# Memory: O(1)
# Runtime: O(n)

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # In: int[] nums
        #     nums[i] represent maximum jump distances
        # Out: int, minimum number of jumps to reach the last position.
        # Con:
        # - There will always be at least 1 position
        # - nums[i] is nonnegative
        # - There is always a valid answer.
        # Edge:
        # - If there's 1 position, we just return 0

        # [2,4,1,1,1,1]
        # 1 --> 4
        # 2 --> 1
        # 1 + 4 --> 1 ( last index )

        # Brute Force:
        # Go through every possible jump pattern
        # Return the path that took the minimum number of jumps!
        # Very inefficient

        # Dynamic Programming: O(n^2)
        # outer loop, you make the jumps
          # inner loop, you compare each possible jump

        # Greedy Solution O(n) time, O(1) space.
        # [2,[4,1,][1,1,1]]
        # 0 to (Jump 1) group
        # (Jump 1) to (Jump 2)

        # Implement
        left = 0
        right = 0
        num_jumps = 0

        while right < len(nums)-1:
            # Decide farthest jump
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest, nums[i])

            # Make the jump
            left = right+1
            right = right+farthest
            num_jumps += 1
        
        return num_jumps
"""
        
# function format
def jump(nums):
    left = 0
    right = 0
    num_jumps = 0

    while right < len(nums)-1:
        # Decide farthest jump
        farthest = 0
        for i in range(left,right+1):
            farthest = max(farthest, nums[i])

        # Make the jump
        left = right+1
        right = right+farthest
        num_jumps += 1
    
    return num_jumps

# Test cases
print(jump([2,4,1,1,1,1])) # 2
print(jump([2,3,1,1,4])) # 2
print(jump([0])) # 0