class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first transpose

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # then mirror image
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[0])-1-j]
                matrix[i][len(matrix[0])-1-j] = temp


        