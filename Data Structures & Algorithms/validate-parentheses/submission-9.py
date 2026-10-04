class Solution:
    def isValid(self, s: str) -> bool:
        # Matches mean s must be even.
        if len(s) % 2 != 0:
            return False

        # Create an empty stack
        stack = []
        closeToOpen = { ')':'(', ']' : '[', '}' : '{' } # Hashmap for O(1) lookup

        # Check if each character is a closing bracket or opening.
        # If opening, add to stack, otherwise verify with the top of the stack
        for c in s:
            # This is a closing bracket, need to check our stack for match
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # We found a match, remove from stack
                else:
                    return False # Does not match
            else:
                stack.append(c) # This is an opening bracket
        
        # If we still have things in the stack, there were opening brackets that did not
        # have a closing one
        return True if not stack else False