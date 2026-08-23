class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = len(matrix) - 1
        c = len(matrix[0]) - 1

        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] <= target <= matrix[mid][c]:
                break

            elif target < matrix[mid][0]:
                high = mid - 1
            
            elif target > matrix[mid][c]:
                low = mid + 1

        else:
            return False

        
        low = 0
        high = c
        r = mid
        while low <= high:
            mid = (low + high)//2
            if target == matrix[r][mid]:
                return True

            elif target < matrix[r][mid]:
                high = mid - 1

            else:
                low = mid + 1

        return False
