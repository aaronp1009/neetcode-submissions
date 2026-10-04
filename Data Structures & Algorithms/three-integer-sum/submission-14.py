class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()

        res = [] # Keep our results
        
        a = 0
        while a < len(nums) and (nums[a] <= 0): # nums[a] has to be negative
            # Skip duplicates, check the previous a only if a is not 0
            if a > 0 and nums[a] == nums[a-1]:
                a += 1 # Increment to make sure we don't infinite loop
                continue
            
            b = a + 1 # Our "left" pointer
            c = len(nums) - 1 # Our "right" pointer

            target = abs(nums[a]) # Our "target" is the positive nums[a]

            while b < c:
                curSum = nums[b] + nums[c]

                if curSum > target:
                    c -= 1
                elif curSum < target:
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]]) # This is where b and c = target (abs(a))
                    b += 1 # Increment b for next loop, moving our left pointer
                    c -= 1 # Decrement c for next loop, moving our right pointer

                    # Now that we've moved our pointers, verify they are not duplicates
                    # if they are, keep incrementing, loop condition remains same
                    while b < c and nums[b] == nums[b-1]:
                        b += 1
                    while b < c and nums[c] == nums[c+1]:
                        c -= 1
            a += 1 # increase a for next iteration
        return res