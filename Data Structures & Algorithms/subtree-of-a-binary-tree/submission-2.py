# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s, t = root, subRoot
        # if t is null, it will always be a subtree of s
        if not t: return True
        # If we hit this statement, t must not be null while s is
        if not s: return False

        # check to see if this t is the same as s
        if self.isSameTree(s, t):
            return True
        
        # If we did not return true above, now check the left and right subtree of s with t
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    
    def isSameTree(self, s, t):
        # base case, both are null, same tree
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            # We are good to go, keep checking
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:
            # Either one was null
            return False