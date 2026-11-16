class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [] # For the backtracking result O(n * 4^n)
        # Our hardcoded hashmap
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Index and current string
        def backtrack(i, cur):
            if len(cur) == len(digits): # Our base case, we found a string the same length as digits
                res.append(cur) # Append our current string
                return
            
            # Loop through each character for this digit
            for c in digitToChar[digits[i]]:
                backtrack(i+1, cur + c) # Increment i, a copy is created when passing down
        
        if digits:
            backtrack(0, "") # Need this so we don't have an empty string in our result

        return res # Result has our answer
