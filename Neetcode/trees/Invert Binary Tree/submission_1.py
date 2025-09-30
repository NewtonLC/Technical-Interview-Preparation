"""
Date: 09/26/2025 17:36
Memory: O(n)
Runtime: O(n)
"""

"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # In: root, binary tree
        # Out: root, new binary tree
        # --> Invert the binary tree --> left children get swapped with right children, for all nodes.

        # Plan: O(n) time and space
        # DFS
        # Iterate through the BT recursively.
        # Swap left and right children by swapping the pointers, then visit left and right children.

        if not root:
            return

        # Invert left subtree
        root.left = self.invertTree(root.left)
        # Invert right subtree
        root.right = self.invertTree(root.right)

        # Swap the pointers
        temp = root.left
        root.left = root.right
        root.right = temp

        return root
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root):
    if not root:
        return

    # Invert left subtree
    root.left = self.invertTree(root.left)
    # Invert right subtree
    root.right = self.invertTree(root.right)

    # Swap the pointers
    temp = root.left
    root.left = root.right
    root.right = temp

    return root

print(invertTree([1,2,3,4,5]))  # Expected: [5,4,3,2,1]
print(invertTree([]))  # Expected: []