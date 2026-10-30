# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx
            
            if preIdx >= len(preorder):
                return None
            
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            # Recursive part
            root.left = dfs(root.val) # Go up to the root for the left subtree
            root.right = dfs(limit) # Go up to the limit for the right subtree

            return root
        
        return dfs(float('inf'))