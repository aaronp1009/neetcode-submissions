# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper
        def valid(node, left, right):
            if not node:
                return True
            
            # Check bounds

            if not (node.val > left and node.val < right):
                return False

            # Recursive call, update min and max bounds
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # Call our recursive function
        return valid(root, float('-inf'), float('inf'))