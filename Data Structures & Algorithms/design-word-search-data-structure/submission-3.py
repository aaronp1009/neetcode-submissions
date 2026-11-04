class TrieNode:
    def __init__(self):
        self.children = {} # For all 26 subtrees of each node
        self.endOfWord = False # To mark end of a word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # Create a root to start from        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: # We need to add it to the prefix tree
                cur.children[c] = TrieNode()
            # Increment to the next level of the tree
            cur = cur.children[c]
        
        # Mark the end node as the end of a word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Define a helper that will do a DFS if we reach a "." to search all subtrees below that level
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)): # Go for the remainder of the word
                c = word[i]

                if c == ".": # Case where we need to dfs
                    for child in cur.children.values(): # Will automatically enumerate
                        if dfs(i+1, child): # Skip our current node
                            return True # We did find a match even with the "." accounted for
                    return False # There was no match after searching all subtrees
                else:
                    # Regular case
                    if c not in cur.children:
                        return False
                    # Increment
                    cur = cur.children[c]
                
            # return the cur node if it reached here with endOfWord. This is the base case
            return cur.endOfWord
        
        # Call our helper
        return dfs(0, self.root)

