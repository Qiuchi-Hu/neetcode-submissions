# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1 is None and list2 is None:
            return None

        newList = ListNode()
        
        if list1.val < list2.val:
            newList.val = list1.val
            newList.next = self.mergeTwoLists(list1.next, list2)
        else:
            newList.val = list2.val
            newList.next = self.mergeTwoLists(list1, list2.next)
        
        return newList

        
        