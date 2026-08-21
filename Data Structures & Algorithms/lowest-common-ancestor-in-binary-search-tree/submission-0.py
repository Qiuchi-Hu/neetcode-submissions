# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        min_node = min(p.val,q.val)
        max_node = max(p.val,q.val)

        if root.val <min_node:
            return self.lowestCommonAncestor(root.right, p,q)
        elif root.val > max_node:
            return self.lowestCommonAncestor(root.left, p,q)
        else:
            return root
        
            

        