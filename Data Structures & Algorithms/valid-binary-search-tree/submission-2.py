# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

TreeNode.min_boundary = -float("inf")
TreeNode.max_boundary = float("inf")

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        valid = True
        if root.left:
            if (root.left.val>=root.val or root.left.val <= root.min_boundary):
                valid=False
            else:
                root.left.max_boundary = root.val
                root.left.min_boundary = root.min_boundary
        
        if root.right: 
            if (root.right.val<=root.val or root.right.val >= root.max_boundary):
                valid=False
            else:
                root.right.min_boundary = root.val
                root.right.max_boundary = root.max_boundary
        
        if not valid:
            return False
        else:

            return (self.isValidBST(root.left) and self.isValidBST(root.right))