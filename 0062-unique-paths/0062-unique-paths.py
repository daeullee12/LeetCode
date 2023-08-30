class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1] * n

        for i in range(1, m):
            newRow = row
            for j in range(1, n):
                newRow[j] = newRow[j - 1] + row[j]
            row = newRow
        
        return row[-1]