# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.node_sep = ","
        self.null_child = "N"

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if root is None:
            return self.null_child
        
        current_tree = str(root.val)+self.node_sep+self.serialize(root.left)+self.node_sep+self.serialize(root.right)
        '''
        current_tree = ""
        current_tree += str(node.val)
        current_tree += self.node_sep

        current_tree += traverse(node.left)
        current_tree += self.tree_sep
        current_tree += traverse(node.right)
        '''
        #print(current_tree)
        return current_tree


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        tree_val_list = data.split(self.node_sep)
        '''
        num_of_nodes = len(tree_val_list)
        print("="*30)
        print(tree_val_list)
        print("num of nodes:", num_of_nodes)
        '''
        index = 0

        def traverse():
            nonlocal tree_val_list,index
            if tree_val_list[index] == self.null_child:
                #print("index: ",index)
                index+=1
                return None
            #print("index: ",index)
            root = TreeNode(val=tree_val_list[index])
            index+=1
            #print("index: ",index)
            root.left = traverse()
            #print("index: ",index)
            root.right = traverse()

            return root

        return traverse()
            

