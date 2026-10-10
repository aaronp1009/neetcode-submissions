# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Go furthest left first, then do the left and right of that
        res = []

        # Start at the root
        def preorder(node):
            if not node:
                return
            
            res.append(node.val) # First add this value
            preorder(node.left)
            preorder(node.right)
        
        # Result should have the answer
        preorder(root)
        return res

