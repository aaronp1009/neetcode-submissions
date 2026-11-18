class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        side_length = total_len // 4
        square = [0] * 4

        if total_len / 4 != side_length:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            seen = set()

            for j in range(4):
                check_side = square[j] + matchsticks[i]
                if check_side <= side_length and check_side not in seen:
                    square[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    # undo/backtrack
                    square[j] -= matchsticks[i]
                    seen.add(check_side)
            return False
        
        return backtrack(0)