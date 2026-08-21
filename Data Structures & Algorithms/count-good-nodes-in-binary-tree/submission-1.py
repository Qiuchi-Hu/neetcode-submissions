# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current_path_max = -float("inf")
        good_nodes = 0
        def dfs(node):
            if node is None:
                return
            
            nonlocal current_path_max
            nonlocal good_nodes
            
            if node.val>=current_path_max:
                good_nodes+=1
                current_path_max = node.val

            record = current_path_max
            
            dfs(node.left)
            current_path_max = record
            dfs(node.right)
            return
        dfs(root)
        return good_nodes

