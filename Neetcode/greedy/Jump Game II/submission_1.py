# Date: 01/29/2026 16:54
# Memory: O(1)
# Runtime: O(n)
# Not working yet

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        # In: int[] nums --> series of jumps
        #     nums[i] --> max jump from position i.
        # Out: int --> MINIMUM number of jumps needed to reach index len(nums)-1
        # Con:
        # - We can jump to any distance up to nums[i].
        # - All nonnegative jumps --> 0's are pits
        # - Always at least one position --> Exactly one position? Return True
        # - There is always a correct answer.
        # Edge:
        # - Exactly one position? Return True

        # Greedy Approach
        # [2,4,1,1,1,1]
        # 0 --> 1 + 4
        # 0 --> 2 + 1
        # 1 --> 5, return 2

        # Greedy Approach but single iteration?
        # 2 --> 
        # [4,0,0,0]
        # 4 --> 3 --> 2 --> 1
        # 

        ptr = 0
        curr_jump = 0
        num_jumps = 0

        while ptr < len(nums)-1:
            if curr_jump + ptr >= len(nums)-1:
                return num_jumps

            if curr_jump < nums[ptr]:
                curr_jump = nums[ptr]
                num_jumps += 1

            ptr += 1
            curr_jump -= 1    
        return num_jumps
"""
        
# function format
def jump(nums):
    # In: int[] nums --> series of jumps
    #     nums[i] --> max jump from position i.
    # Out: int --> MINIMUM number of jumps needed to reach index len(nums)-1
    # Con:
    # - We can jump to any distance up to nums[i].
    # - All nonnegative jumps --> 0's are pits
    # - Always at least one position --> Exactly one position? Return True
    # - There is always a correct answer.
    # Edge:
    # - Exactly one position? Return True

    # Greedy Approach
    # [2,4,1,1,1,1]
    # 0 --> 1 + 4
    # 0 --> 2 + 1
    # 1 --> 5, return 2

    # Greedy Approach but single iteration?
    # 2 --> 
    # [4,0,0,0]
    # 4 --> 3 --> 2 --> 1
    # 

    ptr = 0
    curr_jump = 0
    num_jumps = 0

    while ptr < len(nums)-1:
        if curr_jump + ptr >= len(nums)-1:
            return num_jumps

        if curr_jump < nums[ptr]:
            curr_jump = nums[ptr]
            num_jumps += 1

        ptr += 1
        curr_jump -= 1    
    return num_jumps

# Test cases
# test_case_1 = [2,3,1,1,4]
# test_case_2 = [2,3,0,1,4]
# test_case_3 = [1,2,3]

# Notes:

# My first approach compared the values of each jump locally, then picked the best one.
# However, this is inefficient because we're checking multiple paths that might all work.

# My next approach is to treat the problem like I was driving a car, with gas refill stations.
# If I have less gas then the current position, I need to refill (increment jump count).
# However, this solution did not cover all test cases.