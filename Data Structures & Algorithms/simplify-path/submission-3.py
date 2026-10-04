class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # Keep track of our new path
        paths = path.split('/') # Split on every single / since consecutive slashes don't work anyway

        for cur in paths: # This is each token in our paths list
            if cur == "..":
                if stack: # Only if there is something, we would pop to go up one level
                    stack.pop()
            elif cur != "" and cur != ".": # Empty tokens were consecutive slashes, the period means same directory
                stack.append(cur)
        
        return "/" + '/'.join(stack)

