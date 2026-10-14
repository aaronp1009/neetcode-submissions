# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution, keep track of visited
        stack = [(root, False)] # Tuple will be the node and visited
        res = []

        while stack: # This works since we added our root to it to start
            # Pop from our stack, cur is node, v is visited
            cur, v = stack.pop()
            if cur:
                if v: # We visited so we can just append to our result
                    res.append(cur.val)
                else:
                    # We need to mark this node as visited now, and keep going
                    stack.append((cur, True))
                    # Now do the right and then left
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
                
        
        # Our result array has the result
        return res