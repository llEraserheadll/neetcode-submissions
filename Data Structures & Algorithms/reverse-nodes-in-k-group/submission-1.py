# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grpprev = dummy

        def getkth(curr,k):
            while curr and k > 0:
                curr = curr.next 
                k -= 1
            return curr

        while True:
            kth = getkth(grpprev,k)

            if not kth:
                break
            
            grpnext = kth.next
            curr = grpprev.next
            prev = kth.next

            while curr != grpnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            temp = grpprev.next
            grpprev.next = kth
            grpprev = temp
        
        return dummy.next
