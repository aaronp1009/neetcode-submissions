# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # We will create a string delimited by commas, by creating the
        # string using preorder but keeping track of the NULL values, we 
        # maintain the structure of the tree
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            # Otherwise, we need to do this for the current and left and right subtrees
            res.append(str(node.val)) # convert to a string
            dfs(node.left)
            dfs(node.right)
        
        # Call our dfs on the root
        dfs(root)
        return ",".join(res) # Join them delimited by a comma for deserialization

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convert the data into a list for easy iteration
        vals = data.split(",") # Split by our delimiter
        # We need a global index to keep track
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            # Otherwise, we know this is a legit value
            node = TreeNode(int(vals[self.i])) # convert the string to an int per TreeNode
            self.i += 1

            # Now handle its left and right recursively
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()









