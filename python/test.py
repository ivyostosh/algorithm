# test = []

# if test:
#     print("Empty list is true")
# else:
#     print("Empty list is false")

# ??? need to research
# test_append = [1, 2, 3, 4]
# test_append.append([])
# print(test_append)


# list1 = [1, 1, 2]
# set1 = set(list1)
# print(set1)


# from collections import Counter
# list = [2,4,1,8,2,4]
# dict = Counter(list)
# print(dict)
# dict.subtract([1,2])
# print(dict)


# # BFS

# from collections import deque, defaultdict

# def bfs(root):
#     # Initial value
#     queue = deque([root])
#     distance = {root: 0}

#     # Create graph
#     graph = defaultdict(list)
#     for i, j in root:
#         # Undirected graph
#         graph[i].append(j)
#         graph[j].append(i)
    
#     # Perform BFS
#     while queue:
#         node = queue.popleft()

#         for neighbor in graph[node]:
#             if neighbor not in distance.keys():
#                 distance[neighbor] = distance[node] + 1
#                 queue.append(neighbor)
        
#     return distance


# def dfs_inorder(root):

#     # Initialize values
#     stack = []
#     inorder = []
#     node = root

#     # Perform DFS
#     while node or stack:

#         # Push all left childen to stack
#         while node:
#             stack.append(node)
#             node = node.left
        
#         node = stack.pop()
#         inorder.append(node.val)

#         node = node.right
    
#     return inorder

# list = [1,2,3,2]

# list.remove(2)
# print(list)



# test = 0

# if test:
#     print("hi")


# word = 's'

# print(len(word[1:]))

# print(5.5//2)

# print(int(True))

# print(int(False))


li = [1, 2, 2, 3, 3]
num_highest = max(li, key = li.max)
print(num_highest)