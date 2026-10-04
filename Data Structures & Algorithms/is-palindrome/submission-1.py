class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Make two pointers, left and right
        l = 0
        r = len(s)-1

        while l < r:
            # If left is not valid, increment left ptr
            if not s[l].isalnum():
                l += 1
                continue # go to next iteration
            
            # If right is not valid, increment right ptr
            if not s[r].isalnum():
                r -= 1
                continue # go to next iteration
            
            # Both were valid, now check to see if they are not equal, if so,
            # return False
            if s[l].lower() != s[r].lower():
                return False

            # Increment for next iteration
            l += 1
            r -= 1
        
        # We found no mismatches, they must be palindromes
        return True

                