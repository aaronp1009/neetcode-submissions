# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Let us do a DFS approach where we return a pair [withRoot, withoutRoot]

        def dfs(root):
            if not root:
                return [0, 0]
            
            # Get the deepest left and deepest right pair
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # We know there is a root/node
            withoutRoot = root.val + leftPair[1] + rightPair[1] # Add the withoutRoots
            withRoot = max(leftPair) + max(rightPair) # No restriction

            return [withoutRoot, withRoot]
        
        return max(dfs(root))
