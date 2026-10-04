class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We will do a binary search since the array is sorted to do an O(log(n-k) + k) solution
        l, r = 0, len(arr)-k

        # Do binary search, do not include the equals since l should not equal r for a window
        while l < r:
            m = l + ((r-l) // 2) # Using the distance to the middle method

            if x - arr[m] > arr[m+k] - x: 
                # The right of the window is closer to target, so our window should go rightward
                l = m + 1
            else:
                # The left of the window is closer to the target, so our window should go leftward
                # We set r = m since this else case is basically x - arr[m] was smaller OR equal
                r = m
        
        # left is pointing to the start of the window
        return arr[l:l+k]