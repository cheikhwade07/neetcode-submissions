# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
    
class Solution:
    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q= deque()
        def is_valid_node(node, lower, upper):
            if node.val >= upper:
                return False
            if node.val <= lower:
                return False
            return True

        q.append( tuple( [ root , float('-inf') , float('inf')  ] ) )

        while q: 
            node,lower,upper = q.popleft()
            if node == None:
                continue
            if is_valid_node(node,lower,upper): #O(1)
                q.append(tuple([ node.left , lower , node.val]))    
                q.append(tuple([ node.right , node.val , upper] ))
            else: return False
        return  True
