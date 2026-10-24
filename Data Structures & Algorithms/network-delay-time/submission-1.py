class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_d_root= {i:float('inf') for i in range(1,n+1)}
        edges={i+1:[] for i in range(n)}
        min_d_root[k]=0
        for node,child,time in times:
            edges[node].append( tuple([child , time]) )
        min_edge=0
        
        priority_node=[tuple ( [0,k] ) ]
        visited=set()
        print(edges)
        print(min_d_root)
        print(priority_node)
      
        while priority_node:
            p,n =heapq.heappop(priority_node)
            if n in visited:
                continue
            visited.add(n)
            for c,t in edges[n]:
                c_min , up_min = min_d_root[c] , min_d_root[n] + t
                if up_min < c_min :
                    min_d_root[c] = min_d_root[n] + t
                heapq.heappush( priority_node ,tuple( [ min_d_root[c] , c] ))
        
        max_f_node = max(min_d_root.values())
        if max_f_node == float('inf'):
            return -1
        return max_f_node

        