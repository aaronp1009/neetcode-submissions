class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            # Check if left is alphanumeric
            if not s[l].isalnum():
                l += 1
                continue # Go to the next iteration

            # Check if right is alphanumeric
            if not s[r].isalnum():
                r -= 1
                continue # Go to the next iteration
            
            # Doing lower() on a number string does not affect it
            if s[l].lower() != s[r].lower():
                return False

            # Increment/decrement left or right for next iteration
            l += 1
            r -= 1
        
        # Since there were no mismatches, MUST be a palindrome
        return True

            