# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        level={}
        q= deque()
        q.append( tuple ( [0, root] ) )

        
        #bfs
        while q : 
            l,node = q.popleft()
            if node == None:
                continue
            #append the element to it's list level elment
            level.setdefault(l,[]).append(node.val)
            # check all edges and append them with their respecitve level 
            q.append( tuple( [ l+1, node.left  ]  ) )
            q.append( tuple( [ l+1, node.right  ]  ) )
       
        return list(level.values())
        