class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        res = 0
        maxF = 0

        l = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxF = max(maxF, charCount[s[r]])

            if (r-l+1) - maxF > k:
                charCount[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res