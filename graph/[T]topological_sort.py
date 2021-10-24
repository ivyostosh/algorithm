"""
Extension of Breadth First Search.

Refer to brearth_first_search.py for more documentation.

Rationale: A node should have indegree of 0 (no incomg edges) if they have no dependency.
- We can start from the indegree of 0 node, save them to the order
- Move to their neighbors, remove the edges to indegree 0 nodes, and find more indegree of 0 nodes and then repeat
- The implementation can be done with BFS + calculation / updates of indegrees.

"""

from collections import deque

def get_indegree(graph):

    # Assign initial value
    node_to_indegree = {node : 0 for node in graph}

    # Count indegree
    for node in graph:
        for neighbor in node.neighbors:
            node_to_indegree[neighbor] += 1
    
    return node_to_indegree

def topological_sort(graph):

    # Calculate indegree
    node_to_degree = get_indegree(graph)

    # Assign initial values
    start_node = [node for node in node_to_degree if node_to_degree[node] == 0]
    queue = deque(start_node)
    order = []

    # Perform BFS
    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in node.neighbors:
            # Decrease the indegree as we have removed the indegree 0
            node_to_degree[neighbor] -= 1

            # Load the indegree 0 nodes to queue again and repeat
            if node_to_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there's a cycle
    if len(order) != len(graph):
        return []   # Or something else to indicates there's no topological sort

    return order