class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            
            return True

        l, r = 0, len(s)-1

        while l < r:
            # After the first mismatch, validate the substrings
            if s[l] != s[r]:
                # Try both left and right after deleting to see if any produce a valid palindrome
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
            
            l += 1
            r -= 1
        
        return True