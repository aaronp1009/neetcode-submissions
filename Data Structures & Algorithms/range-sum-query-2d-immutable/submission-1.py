class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for _ in range(ROWS+1)] # Make our sum matrix 1 extra col/row

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # Offset since our sum mat is larger

        bigRect = self.sumMat[r2][c2]
        leftRect = self.sumMat[r2][c1-1]
        topRect = self.sumMat[r1-1][c2]
        topLeftOverlap = self.sumMat[r1-1][c1-1]

        return bigRect - leftRect - topRect + topLeftOverlap 



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#  C0 C1 C2 C3 C4
# [
#  [3, 0, 1, 4, 2] # Row 0
#  [5, 6, 3, 2, 1] # Row 1
#  [1, 2, 0, 1, 5] # Row 2
#  [4, 1, 0, 1, 7] # Row 3
#  [1, 0, 3, 0, 5] # Row 4
# ]

# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)