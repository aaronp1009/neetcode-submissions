class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/") # When splitting on /, empty paths should be skipped, they resulted from multiple /

        for path in paths:
            if path == "..": # Need to check stack, if so, go up one
                if stack:
                    stack.pop()
            elif path != "." and path != "": # Anything . or "" are skipped since they do not get added to our stack
                stack.append(path)

        # Need the / at the front, but not at the end, the front is for the root
        return "/" + "/".join(stack)    