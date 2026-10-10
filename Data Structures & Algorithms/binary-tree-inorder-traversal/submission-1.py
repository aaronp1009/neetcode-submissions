# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative approach, no recursive stack limits, also O(n) still
        res = []
        stack = [] # We will manually manage our stack
        cur = root # start at the root

        # We will go all the way left if there is a valid noot or there are elements in our stack
        while cur or stack:
            # Go all the way right
            while cur:
                # Append this on our stack to keep track of where to go back to
                stack.append(cur)
                cur = cur.left
            
            # Now we are leftmost with no more left nodes, pop to append to result
            cur = stack.pop()
            res.append(cur.val) # Append the value
            # Now set cur to the right subtree to continue the same algorithmt here
            cur = cur.right
        
        # Result should have our answer
        return res