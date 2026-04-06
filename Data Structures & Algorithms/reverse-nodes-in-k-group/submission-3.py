# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getkth(k, prevGroup)
            if not kth:
                break
            
            nextGroup = kth.next
            prev, curr = nextGroup, prevGroup.next

            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next


    def getkth(self, k, current):
        while current and k > 0:
            k -= 1
            current = current.next
        return current
        






        

        


            

            


