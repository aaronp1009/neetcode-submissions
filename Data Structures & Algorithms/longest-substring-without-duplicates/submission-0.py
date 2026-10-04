class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        charSet = set()
        res = 0

        l = 0
        for r in range(len(s)):

            while s[r] in charSet:
                # remove this from the hashmap
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r-l+1)

        return res
