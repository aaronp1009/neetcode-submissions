# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach
        res =  []
        stack = []
        cur = root # Start at root

        while cur or stack:
            # Go all the way left
            while cur:
                # Append this before updating pointer to keep track
                stack.append(cur)
                cur = cur.left
            
            # Now we are leftmost, pop the stack value and append it
            cur = stack.pop()
            res.append(cur.val) # We want the value of cur, not the actual node
            # Now run the same algorithm on the right
            cur = cur.right
        
        # Result should have the answer
        return res
