# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLinkedLists(self, list1, list2):
        newHead = ListNode(0)
        tmpHead = newHead

        while list1 and list2:
            minNode = None
            if list1.val <= list2.val:
                tmpHead.next = list1
                list1 = list1.next
            else:
                tmpHead.next = list2
                list2 = list2.next
            
            tmpHead = tmpHead.next

        if list1:
            tmpHead.next = list1
        else:
            tmpHead.next = list2
        
        return newHead.next

    def mergeKLists(self, lists):
        if not lists:
            return None

        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLinkedLists(
                    lists[i],
                    lists[i + interval]
                )

            interval *= 2

        return lists[0]


          

