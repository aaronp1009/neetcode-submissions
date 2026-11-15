class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking brute force way
        res = []
        part = [] # For each partition we find to add to result

        # Helper for 2 pointer finding if palindrome
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False # Not a palindrome
                l += 1
                r -= 1
            
            return True # We didn't find any mismatches


        def backtrack(i):
            if i >= len(s):
                res.append(part.copy()) # We found an answer and reached end of string
                return
            
            # search every substring now
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    # We found an answer
                    part.append(s[i:j+1]) # Needs to be j+1 since python doesn't include end
                    # Run backtrack
                    backtrack(j+1) # Start at j+1 so we keep searching the rest of the substrings
                    # Cleanup part
                    part.pop()
            
        # Call our backtrack
        backtrack(0)
        return res