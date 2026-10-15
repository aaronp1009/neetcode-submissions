# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # have a global variable to update during recursion
        self.res = 0

        # This is to find the height, or max height basically
        def dfs(curr):
            if not curr:
                return 0 # No height to this

            left = dfs(curr.left)
            right = dfs(curr.right)

            # update our global variable
            self.res = max(self.res, left + right)

            return 1 + max(left, right) # We only want the longest side
        # Run the algorithm
        dfs(root)

        return self.res