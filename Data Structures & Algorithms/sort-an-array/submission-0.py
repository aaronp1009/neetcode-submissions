class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            
            l = arr[L:M+1]
            r = arr[M+1:R+1]

            i, j, k = L, 0, 0

            while j < len(l) and k < len(r):
                if l[j] <= r[k]:
                    arr[i] = l[j]
                    j += 1
                else:
                    arr[i] = r[k]
                    k += 1
                i += 1


            # If there are any elements left in the left array
            while j < len(l):
                arr[i] = l[j]
                j += 1
                i += 1

            # If there are any elements left in the right array
            while k < len(r):
                arr[i] = r[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):

            # If the left pointer = right pointer,
            # nothing to break into
            if l == r:
                return arr

            # Find the middle, integer division
            m = (l + r) // 2

            # Recursive on left to mid
            mergeSort(arr, l, m)
            # Recursive on middle to right
            mergeSort(arr, m+1, r)

            # Call sort on both arrays
            merge(arr, l, m, r)

            return arr

        return mergeSort(nums, 0, len(nums)-1)

            