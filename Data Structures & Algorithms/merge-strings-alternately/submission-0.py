class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        output = ""

        # While in range of both words
        while l < len(word1) and r < len(word2):
            # Take one from word1
            output += word1[l]
            # Then word2
            output += word2[r]

            l += 1
            r += 1

        # Handle remaining letters
        while l < len(word1):
            output += word1[l]
            l += 1
        
        while r < len(word2):
            output += word2[r]
            r += 1

        return output