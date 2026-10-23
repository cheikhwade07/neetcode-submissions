class Solution:
    def countComponents(self,n , edges):
        groups = [n for n in range(n)]
        owner={i:[i] for i in range(n)}
        for x,y in edges:
            if  groups[x] == groups[y]:
                continue
            if x not in owner:
                x = groups[x]
            if y not in owner:
                y = groups[y]
            if len(owner[x]) < len(owner[y]):
                x , y = y,x
                    
            replaced = owner.pop(y)
            groups[y] = x
            for e in replaced:
                owner[x].append(e)
                groups[e] =x	

        return len(owner)
        