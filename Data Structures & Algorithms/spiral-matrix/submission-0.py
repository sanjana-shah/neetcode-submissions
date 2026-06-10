class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while len(ans) < len(matrix) * len(matrix[0]):
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            for i in range(top + 1, bottom+1):
                ans.append(matrix[i][right])

            if len(ans) < len(matrix) * len(matrix[0]):
                for i in range(right - 1, left-1, -1):
                    ans.append(matrix[bottom][i])

            if len(ans) < len(matrix) * len(matrix[0]):
                for i in range(bottom-1, top, -1):
                    ans.append(matrix[i][left])


            left+= 1
            right -=1
            top += 1
            bottom -= 1

        return ans
            

