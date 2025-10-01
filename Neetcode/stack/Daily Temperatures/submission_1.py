"""
Date: 10/01/2025 10:45
Memory: O(n)
Runtime: O(n)
"""

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # In: int[], temperatures
        # Out: int[], result
        # - temperatures and result have the same length
        # - Last element of result will always be 0, there is no following day.
        # E:
        # - One element --> [0]

        # Notes: We want to use a MONOTIC DECREASING STACK.
        # - This is a stack whose values are only decreasing or staying the same.
        # - As we add values to the stack, we check if they are greater.
        # - If greater, we pop from the stack (smallest values popped first) until no values are greater than the current.
        # - After popping, we append the new value(and index!) onto the stack.

        # - We NEED to track both the temperature AND the index in the stack, in order to calculate the distance between the indices.
        # - My previous approach failed because I was trying to ONLY track the temperatures within the stack, then pop them in order.
        # - ^ This would not have worked. I should have been more flexible in how I use stacks, and considered more approaches that
        #   better utilized the stack.

        # Initialize result and stack
        res = [0] * len(temperatures)
        stack = []

        # Loop through each element in temperatures.
        for i, t in enumerate(temperatures):
            # As long as there are elements in the stack that are SMALLER than the current temperature, pop them.
            # When you pop them, take the distance between their index(stored in stack) and the current index, and store it in res.
            # To access the current temperature, get the last element(stack[-1]), then get the temperature(stack[-1][0]).
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            # After popping, append the new temp and index.
            stack.append([t,i])
        
        return res
"""

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([t,i])
    
    return res

# Test cases to be added
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
print(dailyTemperatures([30, 40, 50, 60]))  # Expected: [1, 1, 1, 0]