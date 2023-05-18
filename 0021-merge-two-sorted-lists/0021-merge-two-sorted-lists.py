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
        # TC: O(n+m), MC: O(1)
        dummy = ListNode()
        p = dummy

        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:    
                p.next = list2
                list2 = list2.next
            
            p = p.next

        if list1:
            p.next = list1
            return dummy.next
        elif list2:
            p.next = list2
            return dummy.next

        return dummy.next