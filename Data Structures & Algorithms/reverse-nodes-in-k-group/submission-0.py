# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        ListNode.next = head
        reversePre = dummyNode
        reverseHead = head
        reverseTail = None
        count = 0
        cursor = head

        while cursor is not None:
            count+=1
            if count == k:
                count=0
                reverseTail = cursor
                cursor = cursor.next
                preMarker = reverseHead
                while reverseHead != reverseTail:
                    tmp = reverseTail.next
                    reverseTail.next = reverseHead
                    reverseHead = reverseHead.next
                    reverseTail.next.next = tmp
                reversePre.next = reverseHead
                reversePre = preMarker
                reverseHead = cursor
                reverseTail = None
            else:
                cursor = cursor.next
        
        return dummyNode.next
                

            
