class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        # 0 1 2 3
        self.sumList = [0] *  (self.size+1) # Create a sum list
        # 0 1 2 3 4

        prefix = 0
        for i in range(self.size):
            prefix += nums[i] # Sum of the current is all before
            self.sumList[i+1] = prefix
        

    def sumRange(self, left: int, right: int) -> int:
        return self.sumList[right+1] - self.sumList[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)