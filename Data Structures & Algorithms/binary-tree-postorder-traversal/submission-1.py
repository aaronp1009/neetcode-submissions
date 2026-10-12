# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # No need to keep track of current since we will add to stack
        # keep track of visited as well
        stack = [(root, False)] # (Node, Visited)
        res = [] # To store node values

        while stack: # No need to check current since stack already starts with the root
            # Pop from the stack
            cur, v = stack.pop()
            if cur: # Else case we do nothing
                if v:
                    res.append(cur.val) # We have visited this before, so just add to result
                else:
                    # Have not visited yet or marked it as visited before yet.
                    stack.append((cur, True)) # Since we know this is the second time, mark as True
                    stack.append((cur.right, False)) # Add the right second since top of stack is processed first
                    stack.append((cur.left, False)) # add this to stack as well, we will mark as true next time
        

        return res
                
