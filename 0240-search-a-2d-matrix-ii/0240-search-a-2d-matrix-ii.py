class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) - 1
        i = 0
        j = len(matrix[0]) - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -=1
            elif matrix[i][j] < target:
                i += 1
        return False