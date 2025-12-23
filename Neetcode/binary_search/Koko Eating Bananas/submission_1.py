"""
Date: 12/23/2025 01:26
Memory: N/A
Runtime: N/A

This was a failed attempt at the problem. Here are a few takeaways:
1. I was able to determine that I could use binary search to determine which k-value would work.
2. I did not correctly implement the binary search. The left and right bounds were not updated properly.

What clue was there that a BST would work?
- The k-value can be narrowed down based on whether Koko can finish the bananas in h hours or not.
  - If Koko can finish the bananas in h hours with a certain k-value, then any k-value greater than that will also work.
  - If Koko cannot finish the bananas in h hours with a certain k-value, then any k-value less than that will also not work.

"""

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # In: piles, int[] and h, number of hours.
        # Out: k, int representing the minimum bananas-per-hour eating rate that will allow Koko to finish all bananas in piles.
        # Con:
        # - piles[i] is not sorted in any way, and only consists of positive ints.
        # - piles will not be empty
        # - number of hours won't be less than the number of piles.
        # - k is 100, could Koko eat 100 bananas in 1 hour?
        # - You can eat as many bananas as you want per pile, but can only eat from one pile at a time per hour.
        # Edge:
        # - 

        # Plan:
        # How does k change in relation to len(piles) and h?
        # h = 9, len(piles) = 4 --> 2 
        # h = 4, len(piles) = 4 --> All bananas must be eaten per pile --> k = max(piles)
        # piles[i]?
        # Solving this question --> 

        # Brute Force: Try out k = 1,2,3,4 --> return first k that finishes bananas
        # Don't do this

        # Alg: 1
        # Each pile starts off with values: 1 hour to finish, k = max(piles), h = len(piles)
        # Increase by 1 hour.
        # [1,4,3,2] --> [1,2,2,3,2] --> new k = 3
        # Increase by 1 hour.
        # [1,4,3,2] --> [1,2,2,3,2] --> [1,2,2,2,2,1] --> new k = 2
        # Loop: Increase by 1 hour until we hit h.

        # Alg: 2
        # [1,4,3,2] --> ih = 4, k = 4
        # Cut k in half (rounded up)
        # k = 2, ih increases by the number of piles greater than half k. 
        # Is ih greater than h? --> lower bound of k becomes half k. Then try 3/4 k.
        # less than? --> higher bound of k becomes half k. Then try 1/4 k.
        # equal? --> return k.

        # higher bound --> k = max(piles)
        # lower bound --> k = max(piles) * len(piles)/h rounded up.

        # finding max(piles)? O(n) --> Piles aren't sorted.

        def calculateHours(halfK, piles):
            count = 0
            for pile in piles:
                count += math.ceil(pile / halfK)
            return count

        right = max(piles)
        left = math.ceil(max(piles) * (len(piles) / h))

        while left < right:
            mid = (right+left+1) // 2       # middle of left and right rounded up
            print(left, mid, right)
            if calculateHours(mid, piles) > h:
                right = mid
            elif calculateHours(mid, piles) < h:
                left = mid
            else:
                return mid

        return -1
"""

