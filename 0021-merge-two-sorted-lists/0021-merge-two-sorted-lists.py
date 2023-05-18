# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        first, second = list1, list2
        p = head

        while first is not None and second is not None:
            
            if first.val < second.val:
                p.next = first
                first = first.next
            else:    
                p.next = second
                second = second.next
            
            p = p.next

        if first is None:
            p.next = second
            return head.next
        elif second is None:
            p.next = first
            return head.next


        return head.next