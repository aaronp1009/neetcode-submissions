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
            if cur:
                # Add this node to the res
                res.append(cur.val)
                # Add the right to the stack
                stack.append(cur.right)
                # Keep going
                cur = cur.left
            else:
                cur = stack.pop() # Nothing on the left, cur will be the right
        
        return res