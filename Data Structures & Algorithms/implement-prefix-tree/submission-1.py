class TrieNode:
    def __init__(self):
        self.children = {} # Keep track of all 26 children a-z for this level
        self.endOfWord = False # To mark end of word for the search

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() # Empty node, no children
        

    def insert(self, word: str) -> None:
        cur = self.root # start at root
        
        for c in word:
            if c not in cur.children: # We need to create it
                cur.children[c] = TrieNode()
            # It does exist, so keep incrementing
            cur = cur.children[c]
        # Nothing to return, set the end of word tho for this TrieNode
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root # start at root

        for c in word:
            if c not in cur.children: # Check if this letter is in children
                return False # If we didn't find it, return False
            # It does exist, so keep incrementing
            cur = cur.children[c]
        # In order for search to be true, we must also check if the node we ended at
        # is marked endOfWord
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root # start at root

        for c in prefix:
            if c not in cur.children: # Check if this letter is in children
                return False # If we didn't find it, return False
            # It does exist, so keep incrementing
            cur = cur.children[c]
        # We can return true because we found all letters for this word, no need to check endOfWord
        return True
        