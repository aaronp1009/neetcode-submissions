class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', '}' : '{', ']' : '[' }

        # Iterate through the string, if the character is a closing bracket,
        # check the top of our stack and verify. Else, it is an opening so add to stack
        for c in s:
            # This is a closing bracket
            if c in closeToOpen:
                # Check if our stack is valid first, then peek. If so, then we can pop.
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # It did not match
                    return False
            else:
                # Not a closing bracket, it is opening
                stack.append(c)
        
        # We should have nothing in our stack
        return True if not stack else False
