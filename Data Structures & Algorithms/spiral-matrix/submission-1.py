class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        facing = 0
        visited = set()
        out = []
        x,y = 0,0
        for _ in range(rows*cols):
            print((x,y,facing))
            out.append(matrix[x][y])
            visited.add((x,y))
            nx, ny = x + directions[facing][0], y + directions[facing][1]
            if (nx not in range(rows) or ny not in range(cols)) or (nx,ny)  in visited:
                facing = (facing + 1) % 4
                nx, ny = x + directions[facing][0], y + directions[facing][1]
                
            x,y =  nx,ny
        return out  