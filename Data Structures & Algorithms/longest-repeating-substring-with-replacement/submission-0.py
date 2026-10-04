class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {} # Hashmap to keep track of 26 cap letter counts
        maxF = 0 # our current maximum frequency for the most frequent character seen
        res = 0 # Our result, the maxF + k, it is the size of the longest substring
        
        l = 0 # For our sliding window
        for r in range(len(s)):
            # Add this to our charCount hashmap for this current char
            charCount[s[r]] = 1 + charCount.get(s[r], 0) # Default 0 if the current value doesn't exist
            # Check to see if this count is our new maxF
            maxF = max(maxF, charCount[s[r]])

            # Check if we need to shift our sliding window using the window size r-l+1
            if (r-l+1) - maxF > k:
                # Invalid window, need to shift our pointer and update the charCount hash map
                charCount[s[l]] -= 1
                l += 1
            
            # Update our res with the window length
            res = max(res, r-l+1)

        return res