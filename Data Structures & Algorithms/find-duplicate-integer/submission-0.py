class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Floyd's algorithm to find the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # This is the same as advancing by two since we are using list indices
            if slow == fast:
                break # We found where the cycle intersection
            
        
        # Now find where the cycle starts which is our duplicate... this can be done with a second slow pointer
        slow2 = 0 # It should start at the beginning
        while True:
            slow = nums[slow] # Advance both our slow and slow2, wherever they intersect is our answer (index)
            slow2 = nums[slow2]

            if slow == slow2:
                return slow # Either one works, they point to the same index.