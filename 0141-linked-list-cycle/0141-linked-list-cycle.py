# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Floyd’s Cycle Finding Algorithm, TC O(n)

        slow, fast = head, head

        if head is None:
            return False

        print(head is None and head.next)

        while slow is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
