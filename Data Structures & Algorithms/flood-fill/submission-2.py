class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #bfs in adjacent cell 
        rows = len(image)
        cols = len(image[0])
        visited = set()
        q = deque()
        starting = image[sr][sc]
        q.append(tuple([sr,sc]))
        while q :
            node = q.popleft()
            if node  in visited: continue
            x,y  = node
            directions = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            visited.add(node)
            image[x][y]= color
            for x,y in directions: 
                if x not in range(rows): continue
                if y not in range(cols): continue
                if image[x][y] != starting : continue
                q.append(tuple([x,y]))
        return image




        