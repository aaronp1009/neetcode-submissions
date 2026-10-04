class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k # This ensures our window is k since m is our left part of the window

        while l < r: # binary search, do not include the right boundary since it's the window's end
            m = l + ((r-l) // 2) # Get the middle, this is the left of the window

            if x - arr[m] > arr[m+k] - x: # This means the value to the right is less, so shift our window right
                l = m + 1
            else:
                # value to the left is less, so we would shift our window to the left
                r = m
        
        # left should point to the window start
        return arr[l:l+k]

