# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        level_list = []
        queue = deque()
        queue.append(root)

        while queue:
            current_level = []
            num_of_nodes = len(queue)

            for _ in range(num_of_nodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            
            level_list.append(current_level)
        
        return level_list