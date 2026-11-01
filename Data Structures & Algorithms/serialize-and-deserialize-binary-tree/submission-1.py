# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # Will hold everything before we join by a comma

        # Preorder with null values maintain structure

        def dfs(node):
            if not node:
                res.append("N") # Add "N" to our result
                return
            # Otherwise, we need to convert this node val to string
            res.append(str(node.val))
            # Now call on the node's sub branches following preorder
            dfs(node.left)
            dfs(node.right)
        
        # Call our dfs starting with root
        dfs(root)
        return ",".join(res) # Join the elements of res into one string separated by commas
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # First break our string down to a list of vals
        vals = data.split(",")
        self.i = 0 # Keep track of index in list globally

        def dfs():
            if vals[self.i] == "N":
                self.i += 1 # Increment index variable
                return None # This represents a NULL node
            
            # Otherwise, the value is legit, make a proper node
            node = TreeNode(int(vals[self.i])) # Needs to be a int since it was a string
            self.i += 1 # Make sure to increment index when making a new node
            node.left = dfs() # Run on left first
            node.right = dfs() # Run on the right next
            
            # Return the node for the recursive stack
            return node
        
        # Now call this and return the overall node
        return dfs()