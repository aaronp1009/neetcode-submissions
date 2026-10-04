class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Create a defaultdict to avoid edge cases

        for string in strs:
            char_count = [0] * 26 # Make an empty "list" to keep track of letter counts

            for character in string:
                # Increment the list keeping track of characters
                # if the current string contains that character
                char_count[ord(character) - ord("a")] += 1

            # In our result hashmap, convert our list to a tuple to become immutable
            # it will serve as our key into the hashmap. Then append the whole string
            # to this
            result[tuple(char_count)].append(string)

        # Since order does not matter, convert our results into values
        # our results are a list, we need a list of lists
        return list(result.values())

