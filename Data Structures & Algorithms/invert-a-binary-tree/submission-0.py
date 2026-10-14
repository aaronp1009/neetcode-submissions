# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use recursion, go down to the null case and invert from bottom up

        def invertTree(node):
            if not node:
                return
            
            invertTree(node.left)
            invertTree(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
        
        invertTree(root)

        return root