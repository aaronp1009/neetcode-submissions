# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative approach with inorder traversal works best
        n = 0 # To keep track of when we reach k while popping
        cur = root
        stack = []

        while cur or stack: # Go if cur or stack is not null
            # Go farthest left, this is inorder
            while cur:
                # make sure to append as we travel to the left, this is for popping
                stack.append(cur)
                cur = cur.left
            
            # Now we're furthest left, we reach this when cur is null so pop from stack
            cur = stack.pop()
            # increment n too, this keeps track
            n += 1
            if n == k:
                return cur.val # Return immediately when n == k
            # So if n is not equal to k this iteration, update cur to the right
            cur = cur.right
        