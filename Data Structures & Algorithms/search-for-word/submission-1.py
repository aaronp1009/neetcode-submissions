class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking solution O(n * m * 3^len(word))
        ROWS, COLS = len(board), len(board[0])
        path = set() # Set to keep track of visited

        # define dfs or backtrack function
        def backtrack(r, c, i):
            if i == len(word): # We found a result
                return True
            
            # Base case for not finding

            # If out of bounds, the word at index i is not the same as the board's letter,
            # or we visited it already
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # Case for the fact we have found a good letter, search all 4 directions
            path.add((r, c)) # Add to visited, now search neighbors
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            # We returned so remove from our visited
            path.remove((r, c))

            # Return res
            return res

        # Now call this for each cell
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        # We went through each cell and searched, no result
        return False