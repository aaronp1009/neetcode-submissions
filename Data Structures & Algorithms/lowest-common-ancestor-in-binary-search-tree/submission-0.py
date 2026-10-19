# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            # check if both greater
            if p.val > cur.val and q.val > cur.val:
                # go right
                cur = cur.right
            # check if both smaller
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: # Split occurred, O(logn) TC
                return cur