class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorted nums

        a = 0
        res = []
        # a has to be negative, the abs(a) is technically our target (Two Sum II)
        while a < len(nums) and (nums[a] <= 0):
            # Check to make sure, a is not a duplicate
            if (a > 0) and nums[a] == nums[a-1]:
                a += 1
                continue

            target = abs(nums[a])

            # left and right pointer, b, c
            b = a + 1
            c = len(nums) - 1
            
            while b < c:
                curSum = nums[b] + nums[c]

                if curSum > target:
                    c -= 1
                elif curSum < target:
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1

                    # Check duplicates for b and c, use while loops to keep incrementing
                    while b < c and nums[b] == nums[b-1]:
                        b += 1 # Check the previous b, if equal, keep incrementing
                    while b < c and nums[c] == nums[c+1]: # c+1 is previous since we're going right to left
                        c -= 1                    
            a += 1
        
        return res