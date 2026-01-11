"""
Date: 01/11/2026 12:44
Memory: [To be filled]
Runtime: [To be filled]
"""

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # In: int[]
        # Out: int
        # --> Choose the maximum amount of water a container with i and j heights can store
        # Con: 
        # - All nonneg ints
        # - At least 2 bars
        
        # Two bars "any two bars" --> two pointers solution?
        # Maximum amount of water --> Comparing containers from different points

        # Distance between two bars * height of the shorter bar.

        # Starting two pointer --> start at opposite ends
        # Iterate them inwards while tracking the maximum product.

        # [1,7,2,5,4,12,3,9]
        # Iterate inwards if we see a larger bar?

        # Check A or B which one goes inward
        # Move smaller bar? --> contradiction
        # A = 7, B = 9, 
        # A --> 12, 9 * 2 = 18
        # B --> 12, 7 * 4 = 28
        # Move pointer B.

        # var to track max

        left = 0
        right = len(heights)-1
        max_water = 0

        while left < right:
            left_h = heights[left]
            right_h = heights[right]
            max_water = max(max_water, min(left_h,right_h) * (right-left))

            # If there's a larger height bar, check which bar maximizes the height

            # 2 bars, moving the taller bar only lowers minimum height.
            # moving shorter may increase minimum height? 
            # Either way moving will decrease distance
            
            # Move shorter bar inward.
            if left_h < right_h:
                left += 1
            else:
                right -= 1
        
        return max_water
"""

def maxArea(heights):
    left = 0
    right = len(heights)-1
    max_water = 0

    while left < right:
        left_h = heights[left]
        right_h = heights[right]
        max_water = max(max_water, min(left_h,right_h) * (right-left))

        if left_h < right_h:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test cases to be added
print(maxArea([1,7,2,5,4,12,3,9]))  # Expected: 49
print(maxArea([1,1]))  # Expected: 1