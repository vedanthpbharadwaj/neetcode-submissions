class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # number of rows (num of arrays)
        n = len(matrix[0]) # num of cols (num of elements in the 0th array of matrix)
        low = 0
        high = m*n-1

        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            elif target < value:
                high = mid - 1
            else:
                low = mid + 1

        return False
