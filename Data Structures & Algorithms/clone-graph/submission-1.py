class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        old_to_new = {}

        def clone(original_node):
            if original_node in old_to_new:
                return old_to_new[original_node]

            new_node = Node(original_node.val)

            # 必须先放进去！
            old_to_new[original_node] = new_node

            for neighbor in original_node.neighbors:
                new_node.neighbors.append(clone(neighbor))

            return new_node

        return clone(node)