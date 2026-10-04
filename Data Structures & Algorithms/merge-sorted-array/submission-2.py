class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # Go backwards
        while m > 0 and n > 0:
            # If nums2's last element (of original) is greater
            # put that in our placeholder
            if nums1[m-1] < nums2[n-1]:
                nums1[last] = nums2[n-1]
                n -= 1
            else: # nums1 is larger
                nums1[last] = nums1[m-1]
                m -= 1
            
            # Keep moving our last towards the beginning
            last -= 1
        
        # There may be left over elements in nums2, just continue adding them
        # since they are already sorted
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -=1
        
        return
