class Solution:
     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            visited= set()
            nodes={}
            for p in prerequisites:
                nodes.setdefault(p[0],[]).append(p[1])
                if p[1] not in nodes:
                    nodes[p[1]] = []
            def dfs(node) : 
                if node in visited   :
                    return False		
                
                visited.add(node)
                while nodes[node]:
                    x=dfs(nodes[node].pop())
                    if not x :
                        return False
 
                visited.remove(node)
                return True

            if not prerequisites:
                return True

            for n in nodes.keys():
                if not dfs(n):
                    return False
            
            return True

	
