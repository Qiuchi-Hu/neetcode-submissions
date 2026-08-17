# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head

        dummy = ListNode(0,head)
        groupPrev = dummy
        groupNext = None
        kth = dummy

        while kth:
            for _ in range(k):
                kth = kth.next
                #print(kth.val)
                if kth is None:
                    return dummy.next

            marker  = groupPrev.next
            cur = groupPrev.next
            groupNext = kth.next

            while cur!=marker.next:
                tmp = cur
                cur = cur.next
                tmp.next = groupNext
                groupNext = tmp
            
            groupPrev.next = groupNext
            groupPrev = marker
            kth = marker


