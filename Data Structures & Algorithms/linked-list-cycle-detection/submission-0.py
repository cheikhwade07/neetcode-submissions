# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(selfs,head):
        slow = head 
        fast = head 
        while fast != None and fast.next != None:
            fast = fast.next.next
            if fast == slow : 
                return True 
            slow = slow.next
        return False
        