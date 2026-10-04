class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for o in operations:
            if o == "+":
                # Get prev 2 scores
                sumPrevTwo = stack[-1] + stack[-2]

                total += sumPrevTwo
                stack.append(sumPrevTwo)
            elif o == "D":
                # Get previous score, double it
                doublePrev = 2 * stack[-1]

                total += doublePrev
                stack.append(doublePrev)
            elif o == "C":
                # Remove the previous from the stack, also subtract from our total
                total -= stack.pop()
            else:
                # Add to our stack
                newScore = int(o)
                total += newScore
                stack.append(newScore)

        return total