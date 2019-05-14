"""

133.

Medium

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":
[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

"""


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def dfs(current_node: 'Node'):
            current_node.visited = True
            if not hasattr(current_node, 'copy'):
                current_node.copy = Node(current_node.val, [])
            for neighbor in current_node.neighbors:
                if not hasattr(neighbor, 'copy'):
                    neighbor.copy = Node(neighbor.val, [])
                current_node.copy.neighbors.append(neighbor.copy)

                if not hasattr(neighbor, 'visited'):
                    dfs(neighbor)

        node.copy = Node(node.val, [])
        dfs(node)
        return node.copy
