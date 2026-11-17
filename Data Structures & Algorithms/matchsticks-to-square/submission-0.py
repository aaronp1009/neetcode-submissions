class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        side_length = total_len // 4 # Integer divide...
        square = [0] * 4 # Array to store all four sides

        if total_len / 4 != side_length:
            return False # We got some decimal

        # Sort reverse so that we can quickly identify values that are larger than the side
        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True # base case, we reached the end of matchsticks
            
            # Set for keeping track of used side lengths
            used = set()

            for j in range(4): # Do this for all 4 sides
                # Current side
                check_side = square[j] + matchsticks[i]
                if check_side <= side_length and check_side not in used:
                    square[j] += matchsticks[i] # We can add this value to this side
                    if backtrack(i+1):
                        return True # One of the sides returned
                    # Now backtrack/undo
                    square[j] -= matchsticks[i]
                    used.add(check_side)
            return False # We did not find an answer
        
        return backtrack(0)