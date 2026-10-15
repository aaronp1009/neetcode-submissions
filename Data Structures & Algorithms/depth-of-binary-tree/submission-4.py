# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        stack = []
        stack.append([root, 1]) # Each item on the stack is a node, depth pair

        level = 0

        # While stack exists
        while stack:
            # Get the node and depth
            node, depth = stack.pop()
            if node: # Ensures we are not at a NULL node
                level = max(level, depth) # If this depth is larger, keep going
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        # Level was incremented as we went deeper and deeper
        return level