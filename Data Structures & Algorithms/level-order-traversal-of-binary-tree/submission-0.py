# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # Hold the nested lists of node values per level

        q = deque()
        q.append(root) # Add the root to the queue

        while q:
            # get the length of this queue so far
            qLen = len(q)
            level = [] # This is the number of nodes for this level
            for i in range(qLen): # Loop through the nodes of this level in the queue
                node = q.popleft()
                if node: # This makes sure the queue has no null values in it
                    level.append(node.val) # Add this to the level
                    q.append(node.left)
                    q.append(node.right) # Add in the order left first then right
            # check if level is not empty before adding to our result
            if level:
                res.append(level)
        
        # When loop finishes, return res
        return res