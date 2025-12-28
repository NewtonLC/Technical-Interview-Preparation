"""
Date: 12/28/2025 14:32
Memory: O(1). Heap and Queue hold at most 26 values.
Runtime: O(n * m) where n is the length of tasks and m is the cooldown period.
"""

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # In: str[] tasks, each task is an uppercase english letter, A to Z.
        #     int n --> number of CPU cycles that identical tasks must be separated by. 
        # Out: Minimum num of CPU cycles requires to complete tasks
        # Con: 
        # - tasks is not in order.
        # - Is tasks sorted?
        # - 
        # Edge:
        # - empty tasks --> 0
        # - no need to handle invalid input

        # Plan: 

        # The constraints mean that there are at most 26 different tasks. So what we can do is create a hashmap of the 
        # 26 possible letters and their frequencies.
        
        # Next, we should always process the most frequent task first to minimize the number of CPU cycles.
        
        # A Max-Heap would be the best approach, but I need to refresh myself on how to implement a Max heap.
        # Note: Make sure you understand HOW to implement a Max-Heap, and better recognize when it will be needed.

        # Algorithm:
        # Use MaxHeap and Queue
        # Ex: AAABBCC, n=1
        # MaxHeap: [-3,-2,-2] (Python pops lowest first, so use negative and treat it as positive)
        # Queue: []
        # Time = 0
        # v
        # MaxHeap: [-2,-2]
        # Queue: [-2,2] (-2, and 2 representing the next time we can add it back to the heap)
        # Time = 1
        # v
        # MaxHeap: [-2,-2] (-2 was added back to heap because time = 2)
        # Queue: [(-1,3)] (-1, and 3 representing the next time we can add it back to the heap)
        # Time = 2
        # ... Continue this pattern until MaxHeap is empty. Then return the final time value.

        # Note: You only need to track the numbers in the MaxHeap and Queue. The letters themselves aren't relevant.

        freq_dict = Counter(tasks)
        maxHeap = [-count for count in freq_dict.values()]
        heapq.heapify(maxHeap)      # Converts maxHeap into a heap
        
        time = 0
        queue = deque() # Contains [-count, time] where time is when the value can be added back to the heap.

        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    queue.append([count, time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time
"""

from collections import Counter, deque
import heapq

def leastInterval(tasks, n):
    freq_dict = Counter(tasks)
    maxHeap = [-count for count in freq_dict.values()]
    heapq.heapify(maxHeap)      # Converts maxHeap into a heap
    
    time = 0
    queue = deque() # Contains [-count, time] where time is when the value can be added back to the heap.

    while maxHeap or queue:
        time += 1
        if maxHeap:
            count = heapq.heappop(maxHeap) + 1
            if count:
                queue.append([count, time+n])
        if queue and queue[0][1] == time:
            heapq.heappush(maxHeap, queue.popleft()[0])
    
    return time

# Test cases to be added
print(leastInterval(["A","A","A","B","B","B"], 0))  # Expected: 6
print(leastInterval(["X","X","Y","Y"], 2))  # Expected: 5
print(leastInterval(["A","A","A","B","C"], 3))  # Expected: 9