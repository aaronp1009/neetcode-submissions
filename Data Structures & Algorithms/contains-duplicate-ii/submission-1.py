class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding window technique
        window = set() # Hashset
        l = 0

        for r in range(len(nums)):
            # Ensure our window is not larger than k
            if r - l > k: # problem says <= k so this means window is too large
                window.remove(nums[l]) # Remove left element
                l += 1 # Increment left pointer so new element in window
            
            if nums[r] in window: # check to see if the current element (r) is in our window
                return True # We found a dup
            
            # This is not in our current window, we are safe to add to it
            window.add(nums[r])
        
        # Entire loop finishes, we can return false
        return False
            