class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a monotically decreasing stack
        stack = [] # Pairs with the temp and index, need index to calculate "days" between
        res = [0] * len(temperatures) # This will be our default

        for i, t in enumerate(temperatures): # Allows us to get temperature and index at the same time
            #
            while stack and t > stack[-1][0]: # -1 is the top, 0 is the temp in (temp, index)
                stackT, stackInd = stack.pop()
                # Find the exact index, the days is the substraction
                res[stackInd] = (i - stackInd)
            # We can add this to our stack now, t <= or there is no stack at this point
            stack.append((t, i))
        return res