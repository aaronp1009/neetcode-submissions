# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive is easiest
        if not root:
            return
        # Swap the left and right
        root.right, root.left = root.left, root.right

        # Call the invert tree function on the left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return root
        return root