# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        le = head
        length = 0
        while le != None:
            le = le.next
            length = length + 1

        if length == 1:
            return None

        length -= n
        while length > 0:
            last = cur
            cur = cur.next
            length = length - 1
        if cur.next == None:
            last.next = cur.next
        else:
            cur.val = cur.next.val
            cur.next = cur.next.next
        return head
        
