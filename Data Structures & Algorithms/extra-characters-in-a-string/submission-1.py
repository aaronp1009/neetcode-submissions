class TrieNode:
    def __init__(self):
        self.children = {} # For 26 children on this level
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Increment for next iteration
            cur = cur.children[c]
        
        # Make sure to mark ending node as the end of a word
        cur.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word) # Create our trie
        
        # Top down approach, using DFS recursion

        dp = {len(s):0} # Have this for our base case

        def dfs(i):
            # our memoization portion
            if i in dp:
                return dp[i] # Example: our i is len(s), it returns 0
            
            res = 1 + dfs(i + 1) # Keep going for each "subword"

            # Start at the root of our trie
            cur = trie.root
            for j in range(i, len(s)): # Go until the end of our string
                if s[j] not in cur.children: # We don't even see this letter in our trie
                    break # No point in continuing since the prefix doesn't exist
                # Increment for the next letter
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    res = min(res, dfs(j + 1)) # We want the minimum, we are finding the min number of extra chars
                
            dp[i] = res # Store into our memoized table for caching before returning
            return res
        # Call our helper
        return dfs(0)