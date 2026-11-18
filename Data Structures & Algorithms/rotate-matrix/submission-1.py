class Solution:
    def rotate(self, matrix: List[List[int]]) :
        rows = len(matrix)
        cols =  len(matrix[0])
        clone = [[matrix[i][j] for j in range(cols) ] for i in range(cols)]
        x,y = rows-1,0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = clone[x][y]
                x -= 1
                if x < 0 : 
                    y +=1
                    x= rows-1 
        
        return None  