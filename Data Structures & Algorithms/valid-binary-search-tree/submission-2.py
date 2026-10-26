# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper for DFS
        def valid(node, left, right):
            if not node:
                return True # An empty tree is valid
            
            # We know the node is not null at this point, check cases
            if not (node.val > left and node.val < right): # We are out of bounds
                return False
            
            # Recursive call while updating boundaries
            
            # If going left, the max boundary is the current node, if going right, it is our min boundary
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # Call our helper
        return valid(root, float('-inf'), float('inf'))


