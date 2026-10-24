# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()

        q.append(root) # Add the root

        while q: # queue already has the root
            rightSideNode = None
            qLen = len(q) # Used to iterate for BFS
            for i in range(qLen):
                # Now add all to the next one
                node = q.popleft()
                if node:
                    rightSideNode = node # when this ends, most right side is stored
                    # Add to queue
                    q.append(node.left)
                    q.append(node.right)
            # Add this to res if it exists
            if rightSideNode:
                res.append(rightSideNode.val)
        
        return res
