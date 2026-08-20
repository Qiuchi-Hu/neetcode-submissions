# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue_p = deque()
        queue_q = deque()

        if q:
            queue_q.append(q)
        if p:
            queue_p.append(p)
        
        while queue_q and queue_q and len(queue_q) == len(queue_p):
            q_node = queue_q.popleft()
            p_node = queue_p.popleft()
            if q_node is None and p_node is None:
                continue
            elif q_node and p_node:
                pass
            else:
                return False

            if q_node.val != p_node.val:
                return False
            
            queue_q.append(q_node.left)
            queue_q.append(q_node.right)
            queue_p.append(p_node.left)
            queue_p.append(p_node.right)
        
        if len(queue_q)==len(queue_p):
            return True
        else:
            return False