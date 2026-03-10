"""
Date: Mar 10, 2026 15:14
Memory: 19.50 MB (Beats 80%)       O(n)
Runtime: 0ms (Beats 100%)    O(1) amortized
"""

"""
# In: Stacks (LIFO)
# - Stack 1
# - Stack 2
# - Both stacks only use standard operations: push(to top), peek/pop(from top), size, isEmpty
# Out: 
# - Working MyQueue class. This is functionally a queue (FIFO), but all of its functions are implemented using two stacks.
# - push, pop, peek, empty.

# push() Queue has [1,2,3] and pushes in 4 --> [1,2,3,4]
# Stack 1 has [1,2,3] and we're pushing in 4. --> [4,1,2,3] --> Wrong
# 
# Stack 1 has [1,2,3] and we want to get [1,2,3,4]
# Stack 2 pushes all of Stack 1 --> [3,2,1] --> Stack 2 pushes 4 --> [4,3,2,1]
# Stack 1 pushes all of Stack 2 --> [1,2,3,4]

# pop() Queue has [1,2,3] and pops --> [2,3] and return 1.
# Stack 1 has [1,2,3] and pops --> [2,3] and return 1.

# peek() Queue has [1,2,3] and peeks --> return 1.
# Stack 1 has [1,2,3] and peeks --> return 1.

# empty() Queue is empty --> True. OR Queue has [1,2,3] --> False
# Both stacks are empty. --> True
# One stack is not empty. --> False.

# push --> needs the back element --> push into stack 2.
# pop/peek --> needs the first element --> use stack 1. --> If stack 1 is empty but stack 2 is not, then stack 2 should pop and push into stack 1.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        if not self.stack1:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self) -> int:
        if not self.stack1:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        return self.stack1[-1]

    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        if not self.stack1:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self) -> int:
        if not self.stack1:
            for i in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        return self.stack1[-1]

    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)

# Test cases to be added
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()