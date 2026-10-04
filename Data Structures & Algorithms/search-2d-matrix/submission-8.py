class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First binary search to find the correct row, then binary search for
        # the target in that row

        # rows
        startRow, endRow = 0, len(matrix)-1

        while startRow <= endRow:
            midRow = startRow + ((endRow - startRow) // 2)

            # We know the first int of every row is greater than the last of the previous row
            # so let's use this.
            if matrix[midRow][0] > target:
                # Too large, update our endRow
                endRow = midRow - 1
            elif matrix[midRow][0] < target:
                # Too small, update our startRow
                startRow = midRow + 1
            else: # We found our answer, just return true, it happened to be the first fortunately
                return True
        
        # When the top loop has completed, we know our answer is in startRow - 1
        l, r = 0, len(matrix[0])-1

        while l <= r:
            m = l + ((r-l) // 2)

            if matrix[startRow-1][m] > target:
                # Too large, update our right pointer
                r = m - 1
            elif matrix[startRow-1][m] < target:
                # Too small, update our startRow
                l = m + 1
            else: # We found our answer, just return true, it is in this row
                return True
        
        # We checked each row, each cell and found nothing.
        return False

