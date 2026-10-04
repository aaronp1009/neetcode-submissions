class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for _ in range(ROWS+1)] # Make a bigger matrix for edge cases

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c] # Add all in the current row for matrix
                # above = self.sumMat[r][c+1] the same cell is r+1, c+1 in sumMat but we want the row above
                self.sumMat[r+1][c+1] = prefix + self.sumMat[r][c+1] # Prefix, plus above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        # r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # bigRect = self.sumMat[r2][c2]
        # leftRect = self.sumMat[r2][c1-1]
        # topRect = self.sumMat[r1-1][c2]
        # topLeftOverlap = self.sumMat[r1-1][c1-1]

        # Need to add topLeft since it was subtracted twice.
        return self.sumMat[row2 + 1][col2 + 1] - self.sumMat[row2 + 1][col1] - self.sumMat[row1][col2 + 1] + self.sumMat[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)