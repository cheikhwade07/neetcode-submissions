class Solution:
    def numIslands(self,grid):
        assigned=set()
        numIslands=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if ( grid[i][j]=="1" and tuple([i,j]) not in assigned ):
                    assigned.add(tuple([i,j]))
                    numIslands+=1
                    self.dfs(i,j,grid,assigned)
        return numIslands


    def dfs(self,i,j,grid,assigned):
        position = [(i-1,j), (i+1,j), (i,j-1), (i,j+1) ]
        for x,y in position:
            if ( self.valid_coordinates(x,y,grid ) and grid[x][y]=="1" and tuple([x,y]) not in assigned  ):
                assigned.add(tuple([x,y]))
                self.dfs(x,y,grid,assigned)
        return



    def valid_coordinates(self,i,j,grid):
        if (i >= len(grid) or j >= len(grid[i])):
            return False
        if (i < 0 or  j <   0):
            return False

        return True
        
