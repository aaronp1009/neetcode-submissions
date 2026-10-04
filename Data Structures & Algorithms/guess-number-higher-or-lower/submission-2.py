# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            mid = l + ((r-l) // 2)
            guessRes = guess(mid)

            if guessRes == 0:
                return mid
            elif guessRes == -1:
                # Our guess was too high, move the right number down
                r = mid - 1
            else:
                # Our guess was too low, move the left number up
                l = mid + 1

