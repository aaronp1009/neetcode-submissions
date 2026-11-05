class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        # Set last node to end of word
        cur.endOfWord = True
    
    # Prune to pass TLE
    def pruneWord(self, word):
        cur = self
        nodeAndChildKey = [] # This is a list of (TrieNode, str)

        for c in word:
            nodeAndChildKey.append((cur, c))
            cur = cur.children[c]
        
        for parentNode, childKey in reversed(nodeAndChildKey):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0: # This doesn't have any children, it's a leaf node
                del parentNode.children[childKey]
            else:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = [], set() # List is fine since we prune anyway

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] not in node.children or (r,c) in visit):
                return # Do nothing, out of bounds, not in our list of words, or we visited it already
            
            visit.add((r, c))
            node = node.children[board[r][c]] # Increment to next
            word += board[r][c]

            if node.endOfWord: # This is a word, let's add to result and then prune
                res.append(word)
                node.endOfWord = False
                root.pruneWord(word) # We found our word so let's prune it now from our Trie
            
            # Search all directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Remove this for backtracking so next time we can do a different combination
            visit.remove((r,c))

        # Now call our helper dfs for each cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # Pass empty string since we are building it
        
        # Return the res, it should have the unique list
        return res












