# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root # this will just return null

        # Find the node to delete
        if key < root.val: # Go left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # We found our answer
            if not root.left:
                return root.right # Nothing on the left, just return right
            elif not root.right:
                return root.left # Nothing on the right, return the left
            
            # Now find the min from the right subtree
            cur = root.right
            while cur.left: # Want to go to the MIN of the right subtree recursively
                cur = cur.left
            # Now cur is pointing to the min
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root # Return root, this would have gone in each branch.