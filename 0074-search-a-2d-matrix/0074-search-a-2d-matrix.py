class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            rm = r1 + ((r2 - r1) // 2)
            cm = c1 + ((c2 - c1) // 2)

            if matrix[rm][0] < target < matrix[rm][cm]:
                c2 = cm - 1
            elif target < matrix[rm][0]:
                r2 = rm - 1
            elif matrix[rm][cm] < target < matrix[rm][c2]:
                c1 = cm + 1
            elif target > matrix[rm][c2]:
                r1 = rm + 1
                
            else:
                return True
        return False
