# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node):
        visited=[None]

        # adding pointer to stack until we reach the tail
        while node!= None and node.next != None:
            visited.append(node)
            node=node.next
        #pop stack and reverse list [None]
        tail= node
        while visited and tail != None :  # Node != None shoudln't happen but we'll add it 
            tail.next = visited.pop()
            tail =  tail.next
        return node
        