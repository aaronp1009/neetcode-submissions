from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = Counter(s)
        hashMap2 = Counter(t)
        


        return hashMap == hashMap2