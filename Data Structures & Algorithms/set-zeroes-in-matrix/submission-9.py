class Solution:
    from collections import deque
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited = set() 
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.append((i,j))  
     
        while q :     
            x,y= q.popleft()
            for i in range(rows):
                matrix[i][y] = 0 
            for j in range(cols):
                 matrix[x][j] = 0 

        return None
        
        