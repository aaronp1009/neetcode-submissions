class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        smallestPosNum = 1

        for i in range(n):
            if nums[i] == smallestPosNum:
                smallestPosNum += 1
            
        # Because it's not monotonically increasing, go forwards twice
        for i in range(n):
            if nums[i] == smallestPosNum:
                smallestPosNum += 1

        # Go backwards twice
        for i in range(n-1, -1, -1):
            if nums[i] == smallestPosNum:
                smallestPosNum += 1

        for i in range(n-1, -1, -1):
            if nums[i] == smallestPosNum:
                smallestPosNum += 1
                
        return smallestPosNum