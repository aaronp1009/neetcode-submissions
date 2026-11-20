class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Keep a set for cols, posDiag, negDiag
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n: # We found a solution
                copy = ["".join(row) for row in board] 
                res.append(copy)
                return
            
            # do the backtracking part
            for c in range(n): # n x n board
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue # It's in our set, a queen can attack this already
                
                # We found a valid spot, update our sets
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # Add queen to board
                board[r][c] = "Q"

                backtrack(r+1)

                # Cleanup now after backtrack
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "." # Set back to ., basically undo
        
        backtrack(0)
        return res
