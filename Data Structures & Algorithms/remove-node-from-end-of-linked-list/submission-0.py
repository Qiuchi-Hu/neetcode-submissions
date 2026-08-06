# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        ListNode.index = None
        ListNode.prev = None
        count = 0
        tmp_head = head
        head = ListNode()
        head.next = tmp_head
        tmp_head.prev = head

        while tmp_head.next is not None:
            count+=1
            tmp_head.index = count
            tmp_head.next.prev = tmp_head
            tmp_head=tmp_head.next
        
        count+=1
        tmp_head.index = count

        target_index = count-n+1
        while tmp_head.index != target_index:
            tmp_head = tmp_head.prev
        
        tmp_head.prev.next = tmp_head.next
        if tmp_head.next is not None:
            tmp_head.next.prev = tmp_head.prev
        
        head = head.next
        if head is not None:
            head.prev = None
        return head
