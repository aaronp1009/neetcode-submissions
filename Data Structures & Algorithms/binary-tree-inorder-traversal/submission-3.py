# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # Recursive
        def inorder(root):
            if not root:
                return # Nothing to do, base case
            
            # Go leftmost
            inorder(root.left)
            # Append this value
            res.append(root.val)

            # Now call inorder on the right subtree
            inorder(root.right)
        
        # Call our helper
        inorder(root)

        # Return result
        return res