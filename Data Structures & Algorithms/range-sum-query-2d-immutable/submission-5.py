class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS+1) for r in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c] # Add previous values of the same row
                above = self.sumMat[r][c+1] # r+1, c+1 in our sum matrix is r,c in original, so r is r-1 in original
                self.sumMat[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 +1, row2 + 1, col2 + 1 # Account for offset

        bigRect = self.sumMat[r2][c2]
        topRect = self.sumMat[r1-1][c2]
        leftRect = self.sumMat[r2][c1-1]
        topLeftOverlap = self.sumMat[r1-1][c1-1]

        return bigRect - topRect - leftRect + topLeftOverlap # Make sure to add the overlap since we subtracted twice




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)