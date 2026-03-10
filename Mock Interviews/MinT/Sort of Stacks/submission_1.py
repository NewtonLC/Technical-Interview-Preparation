"""
Date: Mar 10, 2026 16:02
Memory: O(n)
Runtime: O(1) for pop/peek/empty, O(n) for push
"""

"""
# In: 1 additional temporary stack for copying elements
# - We cannot use any other data structures.
# Out: 
# - Define a SortedStack class, which is functionally a stack, but all of its elements remain in a sorted order.
# - push, pop, peek, and isEmpty functions.

# pop, peek, and isEmpty functions --> The same

# push --> needs to be modified to ensure that elements are sorted.

# From example 1: Does pop need to return the element?
# pop --> returns null

# From example 2: We can use pop and peek on an empty stack?
# peek --> returns null
# pop --> does nothing, returns null

# Modified push function
# Stack has [1,2,3,4,5], push 3. --> [1,2,3,3,4,5]
# Regular Stack --> [3,1,2,3,4,5]
# Sorted Stack
# Temp Stack (store all smaller elements in reverse order)
# Sorted Stack has [1,2,3,4,5], pop elements smaller than 3 --> [3,4,5], push 3 --> [3,3,4,5]
# Temp Stack --> [2,1]. pop and push to Sorted --> Sorted has [1,2,3,3,4,5]

class SortedStack:

    def __init__(self):
        self.stk = []
        
    def push(self, val: int) -> None:
        temp_stk = []
        for i in range(len(self.stk)):
            if self.stk[-1] >= val:
                break;
            temp_stk.append(self.stk.pop())
        self.stk.append(val)
        for i in range(len(temp_stk)):
            self.stk.append(temp_stk.pop())

    def pop(self) -> None:
        if not self.isEmpty():
            self.stk.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stk[-1]

    def isEmpty(self) -> bool:
        return not self.stk

sortedStack = SortedStack()
print(sortedStack.push(1))
print(sortedStack.push(2))
print(sortedStack.peek())
print(sortedStack.pop())
print(sortedStack.peek())

sortedStack = SortedStack()
print(sortedStack.pop())
print(sortedStack.pop())
print(sortedStack.push(1))
print(sortedStack.pop())
print(sortedStack.isEmpty())
"""

class SortedStack:

    def __init__(self):
        self.stk = []
        
    def push(self, val: int) -> None:
        temp_stk = []
        for i in range(len(self.stk)):
            if self.stk[-1] >= val:
                break;
            temp_stk.append(self.stk.pop())
        self.stk.append(val)
        for i in range(len(temp_stk)):
            self.stk.append(temp_stk.pop())

    def pop(self) -> None:
        if not self.isEmpty():
            self.stk.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stk[-1]

    def isEmpty(self) -> bool:
        return not self.stk

sortedStack = SortedStack()
print(sortedStack.push(1))
print(sortedStack.push(2))
print(sortedStack.peek())
print(sortedStack.pop())
print(sortedStack.peek())

sortedStack = SortedStack()
print(sortedStack.pop())
print(sortedStack.pop())
print(sortedStack.push(1))
print(sortedStack.pop())
print(sortedStack.isEmpty())