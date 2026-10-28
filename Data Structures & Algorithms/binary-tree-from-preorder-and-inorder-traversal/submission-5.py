# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Track our current position in both traversals globally across recursive calls
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx

            # Base Case 1: All nodes in the preorder list have been processed
            if preIdx >= len(preorder):
                return None
            
            # Base Case 2: The current inorder element matches our structural boundary limit.
            # This means we have completely finished building the current subtree.
            if inorder[inIdx] == limit:
                inIdx += 1  # Consume this value since it marks the end of a subtree boundary
                return None
            
            # 1. Preorder gives us the root of the current subtree immediately
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            
            # 2. Build the left subtree. 
            # Elements in the left subtree cannot cross the current root's value in the inorder sequence.
            root.left = dfs(root.val)
            
            # 3. Build the right subtree.
            # Elements in the right subtree are bounded by the parent's boundary limit.
            root.right = dfs(limit)

            return root

        # Start recursion with an open boundary (infinity) since the absolute root has no limit
        return dfs(float('inf'))