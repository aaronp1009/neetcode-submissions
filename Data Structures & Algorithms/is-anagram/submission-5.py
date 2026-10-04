class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)

        if len_s != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len_s):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT