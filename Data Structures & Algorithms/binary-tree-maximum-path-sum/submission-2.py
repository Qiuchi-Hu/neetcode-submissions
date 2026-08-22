# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -float("inf")

        def traverse(root):
            if root is None:
                return 0 
            
            nonlocal max_path_sum

            left_path_sum = traverse(root.left)
            right_path_sum = traverse(root.right)
            max_path_sum = max(max_path_sum, max(left_path_sum,0)+max(right_path_sum,0)+root.val)
            return max(left_path_sum,right_path_sum,0)+root.val
        
        traverse(root)
        return max_path_sum
            