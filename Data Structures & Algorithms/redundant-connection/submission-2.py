class Solution:
    def findRedundantConnection(self, edges):
        n= len(edges)
        parent = {n : n for n in range(1,n+1)}
        rank= { n: 1 for n in range(1,n+1) }
        def find(n):
            p = []
            while(n != parent[n]):
                p.append(n)
                n = parent[n]
            for c in p:
                parent[c] = n
            return n

        def union(n,e) ->bool:
            n,e = find(n), find(e)
            if n == e:
                return False
            if rank[n] < rank[e]:
                n,e = e,n
            parent[e] = n
            rank[n]+= rank[e]

            return True

        for n,e in edges:
            if not union(n,e):
                return [n,e]

        