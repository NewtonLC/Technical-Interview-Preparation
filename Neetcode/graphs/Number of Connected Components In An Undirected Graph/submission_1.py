"""
Date: [To be filled]
Memory: [To be filled]
Runtime: [To be filled]
"""

"""
class Solution:
    def methodName(self, parameters):
        # Implementation to be added
        pass
"""

def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # In: Undirected graph, n nodes.
        # In: Edges array, edges[i] = [a,b]. a and b are nodes and edges[i] is the edge between them.
        # - Nodes are numbered 0 to n-1

        # Out: Int, total number of connected components in the graph.
        # - Connected component: Basically a subgroup of connected nodes.

        # This problem is a great example of the Union-Find algorithm! Let's use it to solve this problem.
        
        """
        Describing Union Find:

        We'll be maintaining two arrays: Parent and 

        Say we have 5 nodes: 0,1,2,3,4. Edges [[0,1],[1,2],[3,4]]
        Parent --> Starts off at [0,1,2,3,4]. Each index represents that node, each node starts off the 'parent' of itself.
        Rank --> [1,1,1,1,1]. Each index represents that node, each node starts off at rank '1', meaning they have no children.

        When we read [0,1], we note that 1 is a child of 0's parent. 1's parent becomes 0 and 0 becomes rank 2.
        Parent --> [0,0,2,3,4]
        Rank --> [2,1,1,1,1]

        [1,2], we note that 2 is a child of 1's parent. 2's parent becomes 0 and 0 becomes rank 3.
        Parent --> [0,0,0,3,4]
        Rank --> [3,1,1,1,1]

        [0,1], we note that 4 is a child of 3. 4's parent becomes 3 and 3 becomes rank 2.
        Parent --> [0,0,0,3,3]
        Rank --> [3,1,1,2,1]

        IF we encountered, say, [0,2], 2's parent and 0's parent are both 0, so they're already connected. No change is made.

        How can we write this into code?
        """

        # First, we create our two arrays.
        par = [i for i in range(n)]
        rank = [1] * n

        # Then, we need to define our find and union functions.

        # Find: 
        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            # Find the root parent nodes of the two given nodes
            p1, p2 = find(n1), find(n2)

            # If they're equal, then n1 and n2 are already connected. No need to do anything.
            if p1 == p2:
                return 0

            # We are connecting them, so set p1 as the child of p2 or vice versa, depending on which has the higher rank.
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1,n2) # Decrement res by the number of successful unions. This is why we returned 1 for successful union and 0 otherwise.
        return res

# Test cases to be added
# print(function_name(test_input))  # Expected: expected_output
# print(function_name(test_input))  # Expected: expected_output