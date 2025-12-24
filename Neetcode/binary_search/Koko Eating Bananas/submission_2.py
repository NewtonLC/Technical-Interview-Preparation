"""
Date: 12/24/2025 00:08
Memory: O(1)
Runtime: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
"""

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # In: int[] piles --> piles[i] is a pile of bananas.
        #     int h --> number of hours you have to finish all piles
        # Out: k --> MINIMUM banana-per-hour rate that finishes all piles
        # Con:
        # - there will always be at least 1 pile
        # - each pile will always have at least 1 banana
        # - there will always be enough hours to finish every pile
        
        # Brute Force: 
        # Start with k = 1. Check if the number of hours it takes to finish is greater than h.
        # If yes, k=1 is too small. Try k=2.
        # Continue until you find the first k such that the number of hours is not greater than h.

        # BST: We know that...
        # If a k-value works, then every larger k-value will also qualify.
        # If a k-value does not qualify, every smaller k-value will also not qualify.
        # Since we're searching for the SMALLEST value of k that qualifies, we can
        # interpret this as a sorted list!
        # Note: Imagine the possible values of k is an array: [1,2,...,max(piles)]
        # The smallest k that meets x criteria will be somewhere in this array.
        # BST will help us iterate through this array in log(n) time.

        # With BST...
        # If we find a value that works, track it and check left subtree.
        # If we find a value that does not work, check right subtree.

        def calculateHours(k, piles):
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            return count

        right = max(piles)
        left = 1
        res = max(piles)

        while left <= right:
            mid = (right+left) // 2
            numHours = calculateHours(mid,piles)
            if numHours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
"""

import math

def minEatingSpeed(piles, h):
    def calculateHours(k, piles):
        count = 0
        for pile in piles:
            count += math.ceil(pile / k)
        return count

    right = max(piles)
    left = 1
    res = max(piles)

    while left <= right:
        mid = (right+left) // 2
        numHours = calculateHours(mid,piles)
        if numHours <= h:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res

# Test cases to be added
print(minEatingSpeed([3,6,7,11], 8))  # Expected: 4
print(minEatingSpeed([30,11,23,4,20], 5))  # Expected: 30
print(minEatingSpeed([30,11,23,4,20], 6))  # Expected: 23