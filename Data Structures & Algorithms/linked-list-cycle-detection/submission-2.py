# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:   
            slow = slow.next        # Slow Pointer moves 1
            fast = fast.next.next   # Fast pointer moves 2
            if slow == fast:        # If they are equal, theyve reached the same point
                return True
        
        return False