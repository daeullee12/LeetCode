# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # iterative : T(O), M(1)
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
            
        # # recursive : T(O), M(O)
        
        # if not head:
        #     return None
        
        # newHead = head
        # if not head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead

