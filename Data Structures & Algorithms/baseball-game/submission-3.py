class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0
        for o in operations:
            if o == "+":
                res += stack[-1] + stack[-2]
                # Add together to add to our stack
                stack.append(stack[-1] + stack[-2])
            elif o == "C":
                res -= stack.pop() # Simply remove the previous
            elif o == "D":
                # Add double our previous to the stack
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            else:
                res += int(o)
                stack.append(int(o))

        return sum(stack)
