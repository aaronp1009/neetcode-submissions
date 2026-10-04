class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # This is the first string
        prefix = strs[0]
        
        # Loop through all strings after the first
        for i in range(1, len(strs)):
            
            # This keeps track of the index of the strings we are looping through
            j = 0
            
            # We need a while loop where j has to be less than the min between our prefix
            # and the current looped string because the list could start with a shorter word
            while j < min(len(prefix), len(strs[i])):
                if strs[i][j] != prefix[j]:
                    break
                j += 1
                
            prefix = prefix[:j] # Can't be in the while loop because the string in the list could be ""

        return prefix
