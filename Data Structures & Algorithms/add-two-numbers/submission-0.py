# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def calculateVal(self,val1, val2, remaining):
        val = val1+val2+remaining
        if val >=10:
            #print("updating val")
            val -=10
            remaining =1
        else:
            remaining =0
        return val, remaining

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        tmp = answer
        remaining = 0
        while l1 is not None or l2 is not None or remaining!=0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            cur_val,remaining = self.calculateVal(l1_val,l2_val,remaining)
            cur = ListNode(cur_val)
            tmp.next = cur
            tmp = tmp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            #print("cur_val: ",cur_val)
            #print("remaing: ", remaining)
        
        return answer.next
        
        