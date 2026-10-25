# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Need to pass in maxValue, so we'll create a helper dfs
        def dfs(node, maxVal):
            if not node:
                return 0 # No node means not a good node
            
            res = 1 if node.val >= maxVal else 0
            # Compute max value
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Now call it from the outside, starting with root.val is fine since this makes it a "good" node
        return dfs(root, root.val)