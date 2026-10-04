class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # make a default hashmap

        # Loop through strings
        for s in strs:
            count = [0] * 26 # Create a count array populated with 0, 0 count for each a-z

            # Loop through characters of each string
            for c in s:
                # Index into our count array to increment character counts
                count[ord(c) - ord("a")] += 1
            
            # Key into our hashmap, keys must be immutable so convert the count array of size 26
            # to a tuple, then append the current string to this key. Duplicate counts will also be
            # appended to this key
            result[tuple(count)].append(s)

        # Since each value will be returned as a view, convert to a list
        return list(result.values())

