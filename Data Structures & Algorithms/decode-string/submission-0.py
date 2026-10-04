class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]": # This is a closing, pop until top is [
                inner = ""
                while stack[-1] != "[":
                    inner = stack.pop() + inner
                stack.pop()
                
                # Get the k value from stack as well
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                sub = int(k) * inner

                # Append back to our stack now
                stack.append(sub)
            else:
                stack.append(c)
            
        return "".join(stack)
