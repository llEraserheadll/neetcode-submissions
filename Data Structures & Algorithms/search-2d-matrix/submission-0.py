class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            r = mid // cols
            c = mid % cols

            if target < matrix[r][c]:
                right = mid - 1
            elif target > matrix[r][c]:
                left = mid + 1
            else:
                return True
        return False