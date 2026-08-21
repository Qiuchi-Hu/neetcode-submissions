# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        if len(preorder) != len(inorder):
            print("invalid input")
            print(preorder)
            print(inorder)
        '''

        inorder_dict = {
            val: index
            for index, val in enumerate(inorder)
        }

        def traverse(p_start, p_end, i_start, i_end):
            if (p_end - p_start) != (i_end - i_start):
                print("invalid input")
                return None

            if p_end-p_start <=0:
                return None
            
            nonlocal preorder, inorder, inorder_dict
            root = TreeNode(val=preorder[p_start])
            root_index = inorder_dict[preorder[p_start]]
            
            if (root_index < i_start or root_index >= i_end):
                print("invalid root index")
                return None
            
            root.left = traverse(p_start+1, p_start+1+root_index-i_start, i_start, root_index)
            root.right = traverse(p_start+1+root_index-i_start, p_end, root_index+1, i_end)

            return root
        
        return traverse(0, len(preorder),0, len(inorder))
        
        

        