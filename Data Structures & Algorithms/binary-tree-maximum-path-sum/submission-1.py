# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # set result to root, we know it's nonempty
        res = root.val

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            # Get left and right path
            leftPath = dfs(root.left)
            rightPath = dfs(root.right)

            # Account for negative paths, in that case we don't need to take it
            leftMaxPath = max(leftPath, 0)
            rightMaxPath = max(rightPath, 0)

            # result without the split, so both paths included
            res = max(res, root.val + leftMaxPath + rightMaxPath)

            # Return with split, so keep only one side
            return root.val + max(leftMaxPath, rightMaxPath)

        dfs(root)

        return res