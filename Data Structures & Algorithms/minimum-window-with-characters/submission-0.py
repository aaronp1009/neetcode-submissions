class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle edge case
        if t == "": return ""
        
        # Hashmaps for the substring and the chars in current window
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0) # Handle if it doesn't exist already
        
        # Setup sliding window
        have, need = 0, len(countT) # length of hashmap for substring
        res, resLen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            # Add this to our window hashmap
            window[s[r]] = 1 + window.get(s[r], 0)

            # Check if the current character is in our substring, that means we have
            # and the count in our window hashmap is the same as the count in our substring hashmap
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1 # We found one!
            
            # Eviction case for incrementing left
            while have == need:
                # Check to see if this is a better result
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                # This could change what we have compared to our need,
                # if the character we are evicting is one from our substring, we need to reduce our have
                if s[l] in countT and window[s[l]] == countT[s[l]]:
                    have -= 1
                
                # Remove this from the window hashmap now
                window[s[l]] -= 1

                # Safely increment left pointer
                l += 1

        l, r = res
        # Return the substring
        return s[l:r+1] if resLen != float("inf") else ""


                
