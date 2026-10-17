# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are null, they are equal
        if not p and not q:
            return True

        # Otherwise, if both exist, check their values
        if p and q and p.val == q.val:
            # We know this node was good, need to keep checking the subtrees
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else: # Either p or q is empty OR the values do not match
            return False