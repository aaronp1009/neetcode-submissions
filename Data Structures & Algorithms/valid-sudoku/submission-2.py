class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Each key is the position, value is the set
        cols = defaultdict(set) # Each key is the position, value is the set
        squares = defaultdict(set) # Each key will be (r // 3, c //3)

        for r in range(9):
            for c in range(9):
                current_position = board[r][c]

                # If the current spot is a ".", skip the iteration
                if current_position == ".":
                    continue
                
                # Check if the position is in our rows set, cols set, and squares set
                # We integer divide by 3 for the squares to be within the same square
                if (current_position in rows[r] or
                    current_position in cols[c] or
                    current_position in squares[(r // 3, c //3)]):
                    return False
                
                # If not in the set, add to it for next iterations
                rows[r].add(current_position)
                cols[c].add(current_position)
                squares[(r // 3, c //3)].add(current_position)

        # We didn't find anything, so return true
        return True
                
                
