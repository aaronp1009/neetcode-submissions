class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # Keep all our characters

        for c in s:
            if c == "]": # This is a closing, meaning we manipulate our stack
                substring = ""
                while stack and stack[-1] != "[": # Keep updating substring until opening bracket
                    substring = stack.pop() + substring # Can't do +=
                
                # pop the opening bracket
                stack.pop()

                # Get the k value, could be one int or more, so same check
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # Can't do +=
                
                # Add this to our stack but multiplied by k
                stack.append(int(k) * substring)
            else: # All of this just gets added to our stack
                stack.append(c)
        
        return "".join(stack)

