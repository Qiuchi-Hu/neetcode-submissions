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
        
        Node.index = None
        count = 0
        tmp_head = head
        while tmp_head is not None:
            tmp_head.index = count
            count+=1
            tmp_head = tmp_head.next
        
        index_nodeptr = {}

        index_nodeptr[0] = Node(0)
        tmp_nh = index_nodeptr[0]
        tmp_head = head

        def determinePrt(ptr):
            tmp = None
            if ptr is not None:
                if ptr.index not in index_nodeptr:
                    index_nodeptr[ptr.index] = Node(0)

                tmp = index_nodeptr[ptr.index]
            return tmp
        
        while tmp_head is not None:
            tmp_nh.val = tmp_head.val
            tmp_nh.index = tmp_head.index
            
            tmp_nh.next = determinePrt(tmp_head.next)
            tmp_nh.random = determinePrt(tmp_head.random)

            tmp_nh = tmp_nh.next
            tmp_head = tmp_head.next
        
        return index_nodeptr[0]


