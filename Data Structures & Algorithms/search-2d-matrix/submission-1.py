class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l_row = 0 
        r_row = rows -1 
        while l_row <= r_row : 
            middle = (r_row+l_row)//2
            if matrix[middle][0] <= target <= matrix[middle][cols-1] :
                l_col = 0 
                r_col = cols -1 
                while l_col <= r_col:
                    middle_col = (r_col+l_col)//2
                    if target == matrix[middle][middle_col]:
                        return True
                    elif target > matrix[middle][middle_col] :
                        l_col = middle_col + 1
                    elif target < matrix[middle][middle_col] :
                        r_col = middle_col - 1
                break

            elif target > matrix[middle][cols-1] :
                l_row = middle + 1
            elif target < matrix[middle][0] :
                r_row = middle - 1
            

        return False

