# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use a stack to keep track of node and visited
        stack = [(root, False)]
        res = []

        while stack:
            # pop from stack
            cur, v = stack.pop()

            if cur: # Non-null value was popped from stack
                if v: # This means we already visited it twice
                    res.append(cur.val) # Add value to our result
                else:
                    # We need to mark this node as true since this is the second time
                    stack.append((cur, True))
                    # Now add the children of both sides, mark as not visited
                    stack.append((cur.right, False)) # Right first
                    stack.append((cur.left, False))

        return res