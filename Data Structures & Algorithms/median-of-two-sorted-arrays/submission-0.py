class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Re-assign arrays to A and B for clarity. 
        # For an O(log(min(n, m))) solution, we will do binary search on the smaller array
        # swap the arrays A is the larger one, we will run it on A
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        total = len(A) + len(B) # Keep in mind we must subtract 2 later if we want to reference indices
        half = total // 2 # We will use this for partitioning

        # Run binary search on A
        l, r = 0, len(A)-1

        while True: # We are guaranteed a solution
            # middle, index of A
            i = l + ((r - l) // 2)
            # Get the index of B that will be part of the left partition
            j = half - i - 2 # Minus two since our half is based on the total lengths of each

            # Get the left and right of each array for binary search calculations
            Aleft = A[i] if i >= 0 else float('-inf') # Out of bounds, set to negative infinity
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf') # Out of bounds on the right
            Bleft = B[j] if j >= 0 else float('-inf') # Out of bounds, set to negative infinity
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf') # Out of bounds on the right

            # Cases for calculating the median
            if Aleft <= Bright and Bleft <= Aright: # Left partition is smaller than right partition
                # handle odd case
                if total % 2: # This means it did not result in 0, rather 1
                    # Check the minimum of the right
                    return min(Aright, Bright)
                else:
                    # even case
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # Too many elements in the left partition from A, we must reduce it
                r = i - 1
            else:
                # This is for Bleft > Aright, this means too many elements in B,
                # conversely, we need more from A
                l = i + 1
    # Guaranteed to have an answer.
