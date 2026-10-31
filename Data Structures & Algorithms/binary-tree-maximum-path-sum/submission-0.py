# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val # we know it's non-empty

        # This returns the max sum path without split
        def dfs(root):
            nonlocal res
            if not root:
                return 0 # No sum for this

            leftPath = dfs(root.left)
            rightPath = dfs(root.right)
            #  Assume a negative as well, in that case, we don't want it for either side
            leftMaxPath = max(leftPath, 0)
            rightMaxPath = max(rightPath, 0)

            # Compute max sum with split
            res = max(res, root.val + leftMaxPath + rightMaxPath)

            # Return without split
            return root.val + max(leftMaxPath, rightMaxPath)

        dfs(root)
        return res