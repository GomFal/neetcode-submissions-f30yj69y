# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = grouPrev = ListNode(0, head)

        while True:
            kth = self.getKth(k, grouPrev)
            if not kth:
                break
            
            nextGroup = kth.next
            prev, curr = kth.next, grouPrev.next

            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = grouPrev.next
            grouPrev.next = kth
            # Update for the following iteration
            grouPrev = tmp
        
        return dummy.next



    def getKth(self, k, grouPrev):
        while k > 0 and grouPrev:
            k -= 1
            grouPrev = grouPrev.next

        return grouPrev

        






        

        


            

            


