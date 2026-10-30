# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Do this with DFS, use a nested one to get a pair [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left) # Get left pair
            rightPair = dfs(root.right) # Get right pair

            # 1 because 0 is withRoot and we can't include those
            withRoot = root.val + leftPair[1] + rightPair[1]

            # We want the max of both, no restrictions exist
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        
        # Now call this, but remember, it returns a pair so get the max for the int
        return max(dfs(root))