class TrieNode:
    def __init__(self):
        self.children = {} # This is for all 26 characters or subtrees
        self.endOfWord = False # To mark a node that is the end of a word


class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # Empty trie node for the root
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                # Add this node
                cur.children[c] = TrieNode()
            # Increment cur
            cur = cur.children[c]
        
        # Mark this as the end of the word
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        # Define a helper since once we reach a ".", we need to search all subtrees
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)): # Loop through the remaining chars of the word
                c = word[i]
                if c == ".": # We need to search each branch with dfs
                    for child in cur.children.values(): # Get all of the children nodes at this level
                        if dfs(i + 1, child):
                            return True # We could keep continuing taking into account this "."
                    return False # No result found even after looking at all subtrees
                else: # Runs for recursive parts when c is not ".", this is the normal way
                    if c not in cur.children:
                        return False
                    # Keep incrementing, we know this is not a "."
                    cur = cur.children[c]
            
            # Return end of word for this current node
            return cur.endOfWord
        
        # Now call this from outside
        return dfs(0, self.root)
