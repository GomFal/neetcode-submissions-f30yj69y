# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find half of the list with fast and slow pointer:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Slow pointer ends in the middle of the list
        # Slow.next pointer is the start of the second list
        second = slow.next
        prev = slow.next = None # We unlink the lists
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # Now, we re-order it
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        
        



