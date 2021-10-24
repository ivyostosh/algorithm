"""
Breadth First Search

- Use Cases:
    - Topological Sort (100%)
    - Keywords Connected Components (100%)
    - Level Traversal (100%)
    - Shortest Path (100%)
    - Given a set of transformation rules, min steps from initial to final state (100%) ?

- Complexity:
    - Time: O(n + m)
    - Space: O(n)

Key data structure: a queue to store intermediate results, and a dict to store distance (visited).
"""

from collections import deque
# from collections import defaultdict

def breadth_first_search(root, graph):

    # Assign initial values
    queue = deque([root])
    distance = {root: 0}  # If we only care about connectivity (not distance), use set instead.

    # [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
    # if graph hasn't been created, create a graph using dict from edges
    # graph = defaultdict(list)
    # for i, j in edges:
    #     graph[i].append(j)
    #     graph[j].append(i)

    # Perform BFS Traversal
    while queue:
        node = queue.popleft()
        print (node, end = " ") 

        # [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
        # If we have a clear goal, we can set conditions here and return
        # if node meets condition:
          # return something

        for neighbor in graph[node]:
            if neighbor not in distance.keys():
                distance[neighbor] = distance[node] + 1   # Note if we use a set, the method is add()
                queue.append(neighbor)
        
    # print(distance)

    # If returning all points with distance to start point
    return distance

    # If returning all connected points
    # return distance.keys()

    # If returning distance to a target node
    # return distance[target_node]

# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
# Driver Code
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

# Start node: 'A'
breadth_first_search('A', graph)


"""
More questions

[618. Search Graph Nodes](https://www.lintcode.com/problem/618/)
!!! Revisit [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

"""