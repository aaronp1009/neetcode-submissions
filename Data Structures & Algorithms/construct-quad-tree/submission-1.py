"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            # first check if all are the same
            allSame = True

            for i in range(n):
                for j in range(n):
                    # Check if we ever find one not the same
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            
            # If all are same, we don't need to make a new node
            if allSame:
                return Node(grid[r][c], True) # Not a leaf node, no children

            n = n // 2 # Integer divide by 2 for recursive step
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c+n)
            bottomLeft = dfs(n, r+n, c)
            bottomRight = dfs(n, r+n, c+n)

            # using these 4 leaves, return the new node
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        # Call it outside now
        return dfs(len(grid), 0, 0)
