class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                
                if s[l] in countT and window[s[l]] == countT[s[l]]:
                    have -= 1
                
                window[s[l]] -= 1

                l += 1
            
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""