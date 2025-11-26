"""
Date: 11/25/2025 19:00
Memory: [To be filled]
Runtime: [To be filled]
"""

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # In: int[], non-decreasing order. [1,2,3,4,5], [1,1,1,2,3]
        # Out: [index1, index2] --> numbers[index1] + numbers[index2] = target
        # Con:
            # There will ALWAYS be exactly one valid solution.
            # My solution must use constant space.
            # 1-indexed arrays
        # Edge:
            # Empty numbers array? --> N/A, numbers will at least be length 2
            
        # Plan:
        # Alg 1: Brute Force --> O(n^2) time
            # Nested Loop --> For each number in numbers, loop through numbers again and compare
        # Alg 2: Two Pointers --> index1, index2
            # Two pointers on opposite sides.
            # For each loop,
                # Compare the sum of the two pointers to target.
                    # If the sum is higher, then move the right pointer left once.
                    # If the sum is lower, move the left pointer right once.
                    # If the sum == target, return index1, index2
                # If the pointers reach the same number, break the loop and return [-1,-1]
        left = 0
        right = len(numbers)-1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        return [-1,-1]
"""

def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left+1, right+1]
    
    return [-1,-1]

# Test cases to be added
print(twoSum([2,7,11,15], 9))  # Expected: [1,2]
print(twoSum([2,3,4], 6))  # Expected: [1,3]