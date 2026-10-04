class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                # Remove the previous 2 to add them
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                n3 = n1 + n2

                # Add in the correct order to the stack
                stack.append(n1)
                stack.append(n2)
                stack.append(n3)
            elif o == "C":
                stack.pop() # Simply remove the previous
            elif o == "D":
                prev = int(stack[-1])

                stack.append(2*prev)
            else:
                stack.append(int(o))

        return sum(stack)
