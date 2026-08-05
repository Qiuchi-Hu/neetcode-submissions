# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ListNode.node_index = -1

        node_index = 0
        while head is not None:
            if head.node_index == -1:
                head.node_index = node_index
            else:
                return True
            
            node_index+=1
            head = head.next
        
        return False