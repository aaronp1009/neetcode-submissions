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
                return None # Nothing on left
            
            if inorder[inIdx] == limit:
                inIdx += 1
                return None # Nothing on right

            root = TreeNode(preorder[preIdx])
            preIdx += 1 # Move the preIdx count up

            root.left = dfs(root.val) # Go up to the value of the root, recursively
            root.right = dfs(limit) # This builds ALL subtree right nodes

            return root # Return this root for all recursive calls
        
        return dfs(float('inf'))
            
