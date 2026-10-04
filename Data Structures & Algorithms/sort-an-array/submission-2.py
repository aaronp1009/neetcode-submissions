class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Conquer
        def merge(arr, l, m, r):
            # Get the left and right arrays
            left, right = arr[l:m+1], arr[m+1:r+1]

            # Index for base array, left pointer, and right pointer
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                # If left is smaller, take the left
                if left[j] <= right[k]:
                    arr[i] = left[j] # Set array index to left cause smaller
                    j += 1 # Increment left
                else: # Otherwise, right is smaller, do same
                    arr[i] = right[k]
                    k += 1
                i += 1 # Used for the remainder of left/right on the sorted array

            # Get remaining left
            while j < len(left):
                nums[i] = left[j]
                j += 1 # Increment left after taking
                i += 1 # Increment base index after
        
            # Get remaining right
            while j < len(right):
                nums[i] = right[k]
                k += 1 # Increment right after taking
                i += 1 # Increment base index after

        # Divide
        def mergeSort(arr, l, r):
            # Base case
            if l == r:
                return arr
            
            m = (l + r) // 2 # Integer division for index

            mergeSort(arr, l, m) # left up to middle
            mergeSort(arr, m+1, r) # middle+1 up to the right (end)

            # Conquer after recursive divide
            merge(arr, l, m, r)

            return arr

        # Pass in original array to do merge in place
        return mergeSort(nums, 0, len(nums)-1)