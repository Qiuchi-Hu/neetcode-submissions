# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            print("List empty or with one Node")
            return None

        #count = 0
        reverse_head = head
        ListNode.prev = None

        while reverse_head.next is not None:
            #count+=1
            reverse_head.next.prev = reverse_head
            reverse_head=reverse_head.next
        
        #count+=1
        record_head = head
        while reverse_head != record_head and record_head.next != reverse_head:
            tmp_head = record_head
            tmp_tail = reverse_head
            record_head = record_head.next
            reverse_head = reverse_head.prev

            reverse_head.next = None
            tmp_tail.prev = tmp_head
            tmp_tail.next = tmp_head.next
            tmp_head.next = tmp_tail
            record_head.prev = tmp_tail
        


