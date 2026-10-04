class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Base case, we need to make sure strs is legit
        if not strs:
            return ""

        # The first one in the list is our initial prefix
        prefix = strs[0]

        # Loop through the length of the string list
        for i in range(len(strs)):

            # Create an outside index for the words
            # We have to loop between the minimum of the words
            # because the prefix could be smaller
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break # We found a letter that doesn't match
                j += 1 # Increment counter to avoid infinite loop

            prefix = prefix[:j] # Truncate our prefix to that mismatch length
        
        return prefix # Return the prefix
