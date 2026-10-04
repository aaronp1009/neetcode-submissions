class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Go backwards so we don't need to swap things around
        last = m + n - 1

        while m > 0 and n > 0:
            # Since we're going backwards, if this is larger then the largest
            # in nums2, we know it goes at the end of the nums1 array
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # Fill nums1 with leftover nums2
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        
        return

        