# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    	def isValidBST(self, root: Optional[TreeNode]) -> bool:
            def valid_node(node, lower, upper):
                if node == None:
                    return True
                if node.val <= lower: 
                    return False
                if node.val >= upper: 
                    return False
                if not valid_node(node.left,lower,node.val):
                    return False
                if not valid_node(node.right,node.val,upper):
                    return False
                return True
            return valid_node(root,float('-inf'),float('inf'))