class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Always same number of open and closed, based on n
        # if open < n we can add it, if closed < open we can add it
        # if open == closed == n, nothing to add, return this as a possible result

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                # Everything in stack is an element in a list, join to one string
                res.append("".join(stack))
                return
            
            # Case for open
            if openN < n:
                stack.append("(") # Append the open parenthesis
                backtrack(openN+1, closedN) # Call backtrack, increment open by 1
                stack.pop() # Remove from global stack to cleanup
            
            # Case of closed
            if closedN < openN: # only allowed to close however many opens are there
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        # Call it from the outside, 0,0 to start
        backtrack(0,0)
        return res

