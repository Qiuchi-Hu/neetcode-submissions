# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        def traverse_bst(root):
            if root is None:
                return None
            
            nonlocal index
            kth = None
            kth = traverse_bst(root.left)
            if kth is not None:
                return kth

            index +=1
            if index == k:
                return root.val
            
            return traverse_bst(root.right)
        
        return traverse_bst(root)
            