# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global to keep track
        self.res = 0

        # This calculates the height
        def dfs(curr):
            if not curr:
                return 0 # Base case, no height for no node

            # Get the height of the left subtree and the right subtree for this node
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update our global result with this since we want to find the diameter which is the largest left
            # and right height combined going through the same node which we know was curr
            self.res = max(self.res, left + right)

            # The actual logic to keep passing height up the call stack
            return 1 + max(left, right) # Only the max is passed up to the node above.

        # Start the call from the root
        dfs(root)

        return self.res # This has our result
