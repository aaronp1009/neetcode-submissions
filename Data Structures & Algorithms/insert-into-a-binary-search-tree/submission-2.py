# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val) # If no root, just return this as the root
        
        dummy = TreeNode() # This is a dummy which is going to be prev
        cur = root # This is the cur
        prev = dummy
        while cur:
            # Traverse left or right to find where to create the new node
            prev = cur
            if cur.val < val:
                cur = cur.right
            else: # cur.val is greater, we should go left, equal is not part of this problem
                cur = cur.left
        
        # So we found an empty spot for an insert, make new node and insert appropriately
        if prev.val > val:
            # insert as prev's left
            prev.left = TreeNode(val)
        else: # new.val is smaller
            prev.right = TreeNode(val)

        return root