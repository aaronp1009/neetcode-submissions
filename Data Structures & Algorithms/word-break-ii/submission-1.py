class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # backtrack(0)
        #     tries "cat"  → backtrack(3)
        #                         tries "sand" → backtrack(7)
        #                                             tries "dog" → backtrack(10) → [""]
        #                                             → "dog"
        #                         → "sand dog"
        #     → "cat sand dog"

        #     tries "cats" → backtrack(4)
        #                         tries "and"  → backtrack(7) → ... → "dog"
        #                         → "and dog"
        #     → "cats and dog"   
        
        wordDict = set(wordDict) # Convert to a set for O(1) lookup
        cache = {} # Create a cache for repeated work

        def backtrack(i):
            if i == len(s):
                return [""] # Return is supposed to be cached
            if i in cache:
                return cache[i] # We found in our cache, return it
            
            res = []
            for j in range(i, len(s)):
                w = s[i:j+1] # End is not considered, so do +1 in python
                if w not in wordDict:
                    continue # No point in trying this word
                strings = backtrack(j+1) # Start the search for the next word
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            cache[i] = res
            return res
        
        return backtrack(0)