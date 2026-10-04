class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Each key is the position, value is the set
        cols = defaultdict(set) # Each key is the position, value is the set
        squares = defaultdict(set) # Each key will be (r // 3, c //3)

        for r in range(9):
            for c in range(9):
                current_value = board[r][c]

                # If the current spot is a ".", skip the iteration
                if current_value == ".":
                    continue
                
                # Check if the current value is in our rows set, cols set, and squares set
                # We integer divide by 3 for the squares to be within the same square
                squares_key = (r // 3, c //3)
                if (current_value in rows[r] or
                    current_value in cols[c] or
                    current_value in squares[squares_key]):
                    return False
                
                # If not in the set, add to it for next iterations
                rows[r].add(current_value)
                cols[c].add(current_value)
                squares[squares_key].add(current_value)

        # We didn't find anything, so return true
        return True
                
                
