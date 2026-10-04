class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)

        if len_s != len(t):
            return False

        result = defaultdict(list)

        strings = [s, t]

        for i, string, in enumerate(strings):
            count = [0] * 26

            for c in string:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            if i == 0:
                result[key] = 1 # Doesn't matter the value tbh
            else:
                if key not in result:
                    return False

        return True
