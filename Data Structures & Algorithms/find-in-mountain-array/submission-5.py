class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Get peak
        l, r = 0, length-1
        while l <= r:
            m = l + ((r - l) // 2)

            # Get left of mid, mid, and right of mid
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            # We know we found the peak if we are not ascending anymore or descending
            if left < mid < right: # Ascending
                l = m + 1
            elif left > mid > right: # Descending
                r = m - 1
            else: 
                # We found the peak
                break
        peak = m # m is the index of mid and left <= mid >= right

        # Using the peak, search left (ascending)
        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)

            if val > target:
                # reduce our right range to get a smaller val
                r = m - 1
            elif val < target:
                # reduce our left range to get a larger val
                l = m + 1
            else:
                return m # We found the target, return the index

        
        # Using the peak, search right (descending)
        l, r = peak+1, length-1
        while l <= r:
            m = l + ((r - l) // 2)
            val = mountainArr.get(m)

            if val < target:
                # reduce our right range to get a larger val
                r = m - 1
            elif val > target:
                # reduce our left range to get a smaller val
                l = m + 1
            else:
                return m # We found the target, return the index

        # Didn't find target anywhere
        return -1
        