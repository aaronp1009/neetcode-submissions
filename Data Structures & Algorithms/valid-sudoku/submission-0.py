class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def containsDuplicate(str_list: List):
            seen = set()

            for s in str_list:
                if s == ".":
                    continue
                elif s not in seen:
                    seen.add(s)
                else:
                    return True
            return False
        
        # Check the rows
        for i in range(9):
            # Check each row first
            if containsDuplicate(board[i]):
                return False

        # Check columns (extract column i)
        for i in range(9):
            col = [board[r][i] for r in range(9)]
            if containsDuplicate(col):
                return False

        # Check 3×3 boxes
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        box.append(board[r][c])
                if containsDuplicate(box):
                    return False

        return True