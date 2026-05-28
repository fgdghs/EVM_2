class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # {оригинальный_узел: его_клонированный_узел}
        cloned_nodes = {}

        def dfs(old_node):
            if old_node in cloned_nodes:
                return cloned_nodes[old_node]

            copy_node = Node(old_node.val)

            cloned_nodes[old_node] = copy_node

            for neighbor in old_node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))

            return copy_node

        return dfs(node)
