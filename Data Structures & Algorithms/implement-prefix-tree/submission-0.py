# Define a TrieNode, it is a tree node but more than just left, right children
class TrieNode:
    def __init__(self):
        self.children = {} # Hashmap, we will use the character as the key, up to 26 per level a-z
        self.endOfWord = False # Marks if this TrieNode is the end of a word or not

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() # Create a node for the root, there are no children for this yet        

    def insert(self, word: str) -> None:
        cur = self.root # Start at root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() # Create a new node for this letter
            # increment cur
            cur = cur.children[c]
        
        # We are at the end, cur should be marked as end of word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children: # we didn't find it
                return False
            # We found this letter, keep going for all characters in word
            cur = cur.children[c]
        
        return cur.endOfWord # Only if it's the end of a word, return true
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            # Keep going for all letters in prefix
            cur = cur.children[c]
        
        return True
        
        