class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited=set()
        #identifyng rotten 
        max_t=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    p = tuple([ r , c ])
                    rotten.append(tuple([ 0 , p] ))

        #spread bfs 
        while rotten : 
            t,p = rotten.popleft()
            max_t = max(t,max_t)
            x,y = p
            visited.add(p)
            choices = [ [x-1, y ] ,[x, y-1 ] ,[x+1, y ] ,[x, y +1] ]
            for x,y in choices:
                if x not in range(rows) or y not in range(cols):
                    continue
                p_edge = tuple([x,y])
                if p_edge in visited:
                    continue
                if grid[x][y] == 0 :
                            continue
                if grid[x][y] == 1:
                    grid[x][y] = 2	
                    rotten.append( tuple( [t+1,  p_edge] ) )
                    
                
                    
        for r in range(rows): 
            for c in range(cols) : 
                if  grid[r][c] != 1:
                    continue
                return -1
        return max_t

        