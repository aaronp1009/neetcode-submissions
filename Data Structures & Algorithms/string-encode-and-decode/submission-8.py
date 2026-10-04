class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            # First is guaranteed a number
            # Find numbers to indicate length of string
            j = i
            while s[j] != "#":
                j += 1 # Find the numbers to indicate length of string
            
            s_len = int(s[i:j])
            result.append(s[j+1:j+s_len+1])

            i = j + s_len + 1
        
        return result

