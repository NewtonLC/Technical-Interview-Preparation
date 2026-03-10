"""
Question: Given a tree, I want to check if it's a Binary Tree or a Binary Search Tree.

Con:
- Implement the starting of a tree, then we can implement the problem algorithm.

       5
    3     7
  2   4  
    2.5
  2.1

5                                --> 2
root --> .left --> .left --> ... --> no left child

2                   2.5                     2.1
Leftmost Node --> Node's right child's --> successor

Node:
    node.val
    node.left
    node.right

Tree:
    root node    

In: Tree --> Nodes with left and right pointers
Out: Boolean --> False: Binary Tree, True: BST
- (Want to use this in another program)

Con:
- Input will either be a BT or BST
- Difference between a BT and BST?
BST --> Sorted
Each node in any given node's left subtree will be smaller
Each node in any given node's right subtree will be larger
If the tree does not follow these rules, we should return false.

Traversal --> Full Tree traversal
Pre-order, in-order, post-order



Edge:
- Empty Tree? --> False, BT
- Null? --> False, BT
- One node? --> BST

"""

class Node:
    val = int
    left = Node
    right = Node

class Tree:
    root = Node

def analyzeBinaryTree(root):
    """
    BST --> Sorted
    Each node in any given node's left subtree will be smaller
    Each node in any given node's right subtree will be larger
    If the tree does not follow these rules, we should return false.
    """
    if not root:
        return False
    if not root.left and not root.right:
        return True

    """
       5
    3     7
  2   4  
    """

    # Recursive case

    # Find successor
    # right child's leftmostNode if right child exists
    # Parent if right child does not exist

    
        
