# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # We stablish the difference of n between the left and right node
        while n > 0:
            right = right.next
            n -= 1
        
        # We move the right node until the end of the list
        while right:
            right = right.next
            left = left.next
        # Now, we have left just before the nth node
        left.next = left.next.next

        return dummy.next




