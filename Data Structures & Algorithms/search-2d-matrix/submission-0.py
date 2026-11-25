class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0 
        r = rows*cols - 1

        while l <= r:
            middle = (r+l)// 2
            x_m = middle // cols
            y_m = middle % cols
            val = matrix[x_m][y_m]
            if val == target:
                return True
            elif target > val :
                l = middle + 1
            elif target < val : 
                r = middle - 1
        return False

        '''
        l = 4
        r = 4
        middle = 4
        val = 10
        return True


        
        

        '''
            


