class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # For O(log(min(n, m))) make sure A is the minimum, we will run binary search on it
        A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(A) + len(B)
        half = total // 2

        # B.S. on A
        l, r = 0, len(A)-1

        while True:
            i = l + ((r - l) // 2)
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # Left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # even case
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else: # odd case
                    return min(Aright, Bright)
            elif Aleft > Bright:
                # Too many elements in left partition from A, reduce A
                r = i - 1
            elif Bleft > Aright:
                # Too little from A, increase A
                l = i + 1
