# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS
        
        # Uses a queue, we will go level by level
        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0 # Start at 0

        while q:
            # iterate for each node in queue and add their children, increase level each time
            for i in range(len(q)):
                # pop the left, FIFO where we will use it to add the children
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level
