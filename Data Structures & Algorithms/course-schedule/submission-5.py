class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 == unvisited , 1== exploring 2== explored
        n= numCourses
        states=[0 for i in range(n) ]
        edges={i:[] for i in range(n)}
        for v,e in prerequisites:
            edges[v].append(e)

        def dfs(n) ->bool:
            print(n)
            if states[n] == 1:
                return False
            
            states[n] = 1
            for e in edges[n]:
                if states[e]==2 :
                    continue
                if not dfs(e) : 
                    return False
            states[n] = 2
            return True
            
        for i in range(n):
            if not dfs(i):
                return False
        return True

        