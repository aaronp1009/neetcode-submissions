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

        # Keep loop going until stack is empty and cur is null
        while cur or stack:
            # for the current node, add it to res, store the right for the future
            # and keep going left
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                # Pop the stack to travel right subtree
                cur = stack.pop()
        
        # return res
        return res