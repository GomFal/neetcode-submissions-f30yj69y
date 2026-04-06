# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # We use 2 pointers to obtain the middle of the list
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        print(sp.val)
        # Now that we have the sp at the middle of the list, we can reverse the second list
        second = sp.next
        # To unlink both lists
        sp.next = None
        
        # We reverse the second list
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        
        

        




        

            




        



