# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node):
        prev = None
        #[None]<-[0] [1]
        while node!= None and node.next!=None :
            next_n=node.next
            node.next= prev
            prev=node
            node=next_n
        if node != None:
            node.next = prev
        return node
        