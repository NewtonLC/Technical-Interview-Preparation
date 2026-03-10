Difficulty: Medium

Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty. When the stack is empty, peek should return -1.

Example 1:
```
 Input:

["SortedStack", "push", "push", "peek", "pop", "peek"]

[[], [1], [2], [], [], []]

 Output:

[null,null,null,1,null,2]
```

Example 2:
```
 Input:

["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]

[[], [], [], [1], [], []]

 Output:

[null,null,null,null,null,true]
```