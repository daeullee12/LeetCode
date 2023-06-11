class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            rm = r1 + ((r2 - r1) // 2)
            cm = c1 + ((c2 - c1) // 2)

            if matrix[rm][cm] > target:
                if matrix[rm][0] > target:
                    r2 = rm - 1
                else:
                    c2 = cm - 1
            elif matrix[rm][cm] < target:
                if matrix[rm][c2] < target:
                    r1 = rm + 1
                else:
                    c1 = cm + 1
                
            else:
                return True
        return False

# matrix[r1][c1] matrix[r1][cm] matrix[r1][c2]
# matrix[rm][0] matrix[rm][cm] matrix[rm][c2]
# matrix[r2][0] matrix[r2][cm] matrix[r2][c2]