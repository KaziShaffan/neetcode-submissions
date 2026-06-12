class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        whole_rows = len(matrix)
        whole_cols = len(matrix[0])

        left = 0
        right = (whole_rows * whole_cols) - 1

        
        while left <= right:
            mid = (left + right) // 2

            row = mid // whole_cols
            col = mid % whole_cols

            current = matrix[row][col]
            

            if current == target:
                return True
            elif current < target:
                left = mid + 1
            else:
                right = mid - 1



        return False
