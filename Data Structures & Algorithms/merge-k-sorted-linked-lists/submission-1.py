# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        def merge(l1,l2):
            dummy = ListNode()
            left = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    left.next = l1
                    l1 = l1.next
                else:
                    left.next = l2
                    l2 = l2.next
                left = left.next
            
            if l1:
                left.next = l1
            else:
                left.next = l2
            
            return dummy.next
        if len(lists) > 0:
            step = 1
            while step < n:
                for i in range(0,len(lists) - step,step*2):
                    lists[i] = merge(lists[i],lists[i+step])
                step*= 2
            return lists[0]
