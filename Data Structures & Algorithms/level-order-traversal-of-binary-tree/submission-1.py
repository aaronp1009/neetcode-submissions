# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # Stores the result

        q = deque() # Use collections double ended queue
        q.append(root) # Add our root to the queue currently

        while q: # Go until queue is not empty
            qLen = len(q) # get the length of the current queue, this is how we go level by level
            level = [] # Empty for each BFS level
            for i in range(qLen): # The i doesn't matter
                node = q.popleft() # Get the left of the queue
                if node: # Makes sure we aren't adding empty nodes to our level
                    level.append(node.val) # We want the value of the node
                    # Now add the children to the queue in correct order
                    q.append(node.left)
                    q.append(node.right)
            # After the for loop for the level, add this to the result ONLY if not empty
            if level:
                res.append(level)
        
        # When while loop finishes, result has answer
        return res