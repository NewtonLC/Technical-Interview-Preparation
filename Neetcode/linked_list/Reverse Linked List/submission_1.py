"""
Date: 09/04/2025 15:08
Memory: O(1)
Runtime: O(N)
"""

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        In: LL --> head
        Out: LL --> new head
        Con:
        - LL needs to be reversed --> new head must be the current tail
        Edge:
        - None --> None
        - One node --> Same node

        Alg 1:  O(N) space and time
        - Create a new LL
        - Loop through the nodes in the LL
            - Put them in reverse order in the new LL
        - Return the new LL

        Alg 2: O(N) time? O(1) space
        -       v     V     V
        - 1 --> 2 --> 3 --> 4 ==> 4 --> 3 --> 2 --> 1
        '''

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

# Test cases to be added
# print(function_name(test_input))  # Expected: expected_output
# print(function_name(test_input))  # Expected: expected_output

