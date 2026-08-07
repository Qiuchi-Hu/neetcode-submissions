"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # interving nodes
        tmp = head
        while tmp is not None:
            new = Node(tmp.val)
            new.next = tmp.next
            tmp.next = new
            tmp = new.next
        
        tmp = head
        while tmp is not None:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        tmp = head
        newHead = head.next
        copy = head.next
        while tmp is not None:
            tmp.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            tmp = tmp.next
            copy = copy.next
        
        return newHead



