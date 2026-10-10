# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach
        res = []

        def inorder(root):
            if not root:
                return # This is our base case

            # Inorder is going as left as possible
            inorder(root.left)
            # Once that call finishes, we are leftmost, so append this value
            res.append(root.val)
            # After, call our inorder on this node's right subtree
            inorder(root.right)
        
        # Our res has the answer
        inorder(root)
        return res