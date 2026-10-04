class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False # No way there can be any permutation
        
        s1Count, s2Count = [0] * 26, [0] * 26 # Store counts
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        
        # Find current matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            # If we match all 26, we found a valid permutation or anagram of s1 in s2.
            if matches == 26:
                return True
            
            # Update the matches counts, first for the right pointer
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: # They match, so add a match
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1 # Adding this to the s2Count[index] caused a mismatch
            
            # Update the left pointer
            index = ord(s2[l]) - ord('a')
            s1Count[index] += 1
            if s1Count[index] == s2Count[index]: # They match, so add a match
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1 # Adding this to the s2Count[index] caused a mismatch

            l += 1
    
        return matches == 26