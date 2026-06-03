class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Set indicators for first row and column
        first_row = False
        first_col = False
        rows, cols = len(matrix), len(matrix[0])
        first_row = 0 in matrix[0]
        first_col = any(row[0] == 0 for row in matrix)

        # Set row and column indicators to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Set inner matrix values to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Set first row to all zeroes if necessary
        if first_row:
            matrix[0] = [0] * cols

        # Set first column to all zeroes if necessary
        if first_col:
            for row in matrix:
                row[0] = 0