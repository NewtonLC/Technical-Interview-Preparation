"""
Date: 03/09/2026 15:43
Memory: 28ms (Beats 100%)       O(n log k)
Runtime: 7.7 MB (Beats 100%)    O(k)
"""

"""
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # In: int[] nums unsorted, int k

        # Out: int --> kth largest element in the array

        # Con:
        # - 1 <= k <= nums.length <= 10000 --> k cannot be out-of-bounds.
        # - Numbers are not always distinct

        # Ex:
        # - Input: nums = [2,3,1,5,4], k = 2
        # - Output: 4, 4 is the 2nd-largest number in nums.

        # Approach 1: Sort
        # Sort nums() --> nums = sort(nums)
        # Take the k-th element.
        # Time: O(n logn)
        # Space: O(1)

        # Approach 2: Min-Heap
        # The Min Heap will store k-number of elements
        # It stores elements and keeps the smallest element at the top.
        # When we add an element to the Min-Heap, it takes O(logk) time since we store k elements in it.
        # Retrieving the top element takes O(1) time since it's at the top.
        # We plan to store the largest elements from nums in this min-heap, 1st - kth.
            # At the end of the algorithm, the kth largest element will be the smallest element in the min-heap.

        # When looping through nums, if we encounter a number smaller than the top of minHeap...
            # It's not relevant to our answer at all, so we can ignore it.
        # If we encounter a number larger than the minHeap...
            # We want to add this number to our heap, but also remove the top of the heap.
                # We can perform this function most efficiently by running heapq.heappushpop(minHeap, num)
        # At the end of the loop, return heapq.pop(minHeap)

        # Let's do the minHeap approach.

        # Initialize minHeap to be the first k elements of nums.
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            if num > minHeap[0]:
                heapq.heappushpop(minHeap, num)
        
        return heapq.heappop(minHeap)
"""

import heapq

def findKthlargest(nums, k):
    minHeap = nums[:k]
    heapq.heapify(minHeap)

    for num in nums[k:]:
        if num > minHeap[0]:
            heapq.heappushpop(minHeap, num)
    
    return heapq.heappop(minHeap)

# Test cases to be added
print(findKthlargest([2,3,1,5,4], 2))  # Expected: 4
print(findKthlargest([2,3,1,1,5,5,4], 3))  # Expected: 4