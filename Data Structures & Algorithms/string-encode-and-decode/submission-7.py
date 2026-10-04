class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Prepend a dummy char (e.g., space) so [""] becomes " " instead of ""
        # This ensures the encoded string is non-empty for [""] but empty for []
        delimited = " " + "!123".join(strs)

        string_list = list(delimited) # turn to a list to iterate
        
        for i, c in enumerate(string_list): # Minus each character ordinal
            string_list[i] = chr(ord(c) - 5)

        result = "".join(string_list) # Join all characters in the list

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        string_list = list(s) # Convert string to list

        for i, c in enumerate(string_list): # Up each character ordinal
            string_list[i] = chr(ord(c) + 5)
        
        delimited_str = "".join(string_list) # Get one long string

        result = delimited_str[1:].split("!123") # Split by !123

        return result

