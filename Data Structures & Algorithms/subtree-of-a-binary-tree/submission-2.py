# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
global subTree_check
subTree_check = False
class Solution:
    '''
    def printTree(self,root):
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print("="*10)
            print("val: ",current.val)
            print("left: ",current.left.val if current.left else None)
            print("right: ",current.right.val if current.right else None)
    '''
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        global subTree_check

        if root is None and subRoot is None:
            return True

        if root and subRoot:
            if subTree_check and root.val != subRoot.val:
                return False
            current_isSubtree = False
            if root.val == subRoot.val:
                subTree_check = True
                current_isSubtree = (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right))
                subTree_check = False
            
            return current_isSubtree or (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        else:
            return False