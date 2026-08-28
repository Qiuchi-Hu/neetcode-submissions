"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        original_nodes = {}
        new_nodes = {}

        def clone(original_node):
            nonlocal original_nodes, new_nodes
            if not original_node:
                return None
            if original_node.val in original_nodes and original_node in original_nodes[original_node.val]:
                return new_nodes[original_node]
            
            if not original_node.val in original_nodes:
                original_nodes[original_node.val] = [original_node]
            else:
                original_nodes[original_node.val].append(original_node)
            
            new_node = Node(val = original_node.val)
            new_nodes[original_node] = new_node
            new_neighbours = []

            for neighbor in original_node.neighbors:
                new_neighbours.append(clone(neighbor))
            new_node.neighbors = new_neighbours

            return new_node

        return clone(node)
