# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # overall function returns a bool so can't do self. and call it

        # Defining a helper, we will return [Bool, Height]
        def dfs(node):
            # base case, the bool represents if balanced
            if not node:
                return [True, 0]
            
            # Now call this on the left and right branches
            left, right = dfs(node.left), dfs(node.right)

            # Check if the node is balanced, we are in the recursive call stack
            # this checks if the left is balanced, right is balanced, and then checks if
            # both heights are within 1 of each other
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            # Now we return, remember, we are returning a [Bool, Height]
            # the height is the max of the two, 1 is the index for the height
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0] # We expect the bool which is the balanced, so we this is "balanced" from the root
