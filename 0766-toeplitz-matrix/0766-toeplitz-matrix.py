class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        if n == 1:
            return True
        m = len(matrix[0])
        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True