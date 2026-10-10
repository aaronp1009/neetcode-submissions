# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach
        res = []
        stack = []
        cur = root

        while cur or stack:
            # if our node is not null, add to result and append the right to the stack
            if cur:
                res.append(cur.val) # Add this to our result
                stack.append(cur.right) # We need this to know to do everything on the same level later
                cur = cur.left # Keep going left now
            else: # We reached all the way left, now process the right branches in our stack
                cur = stack.pop()
            
        
        return res
