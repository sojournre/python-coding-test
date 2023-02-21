# #
# # Complete the 'minimumTreePath' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. 2D_INTEGER_ARRAY edges
# #  3. INTEGER_ARRAY visitNodes
# #

# from collections import deque
#
# def minimumTreePath(n, edges, visitNodes):
#     # Create an adjacency list to represent the unweighted tree
#     adj_list = {i: [] for i in range(1, n + 1)}
#     for edge in edges:
#         adj_list[edge[0]].append(edge[1])
#         adj_list[edge[1]].append(edge[0])
#
#     # Start a BFS from node 1 and visit all nodes in the visitNodes array
#     visited = set()
#     distances = {1: 0}
#     queue = deque([1])
#     while queue:
#         curr_node = queue.popleft()
#         visited.add(curr_node)
#         for neighbor in adj_list[curr_node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 distances[neighbor] = distances[curr_node] + 1
#     for node in visitNodes:
#         if node not in distances:
#             return -1
#
#     # Calculate the minimum path length by summing up the minimum distances between adjacent nodes in the visitNodes array
#     visitNodes = [1] + sorted(visitNodes) + [n]
#     min_path_length = 0
#     for i in range(len(visitNodes) - 1):
#         u, v = visitNodes[i], visitNodes[i + 1]
#         min_path_length += distances[u] + distances[v] - 2 * distances[lca(adj_list, u, v)]
#
#     return min_path_length
#
#
# # Function to find the lowest common ancestor of two nodes in a tree
# def lca(adj_list, u, v):
#     depth = {1: 0}
#     parent = {1: None}
#     stack = [1]
#     while stack:
#         curr_node = stack.pop()
#         for neighbor in adj_list[curr_node]:
#             if neighbor != parent[curr_node]:
#                 parent[neighbor] = curr_node
#                 depth[neighbor] = depth[curr_node] + 1
#                 stack.append(neighbor)
#     while depth[u] > depth[v]:
#         u = parent[u]
#     while depth[v] > depth[u]:
#         v = parent[v]
#     while u != v:
#         u = parent[u]
#         v = parent[v]
#     return u


# from collections import deque
#
# def minimumTreePath(n, edges, visitNodes):
#     # Create an adjacency list to represent the unweighted tree
#     adj_list = {i: [] for i in range(1, n+1)}
#     for edge in edges:
#         adj_list[edge[0]].append(edge[1])
#         adj_list[edge[1]].append(edge[0])
#
#     # Start a bidirectional BFS from nodes 1 and n and visit all nodes in the visitNodes array
#     visited_forward = set()
#     distances_forward = {1: 0}
#     queue_forward = deque([1])
#     visited_backward = set()
#     distances_backward = {n: 0}
#     queue_backward = deque([n])
#     while queue_forward or queue_backward:
#         if queue_forward:
#             curr_node = queue_forward.popleft()
#             visited_forward.add(curr_node)
#             if curr_node in visited_backward:
#                 break
#             for neighbor in adj_list[curr_node]:
#                 if neighbor not in visited_forward:
#                     queue_forward.append(neighbor)
#                     distances_forward[neighbor] = distances_forward[curr_node] + 1
#         if queue_backward:
#             curr_node = queue_backward.popleft()
#             visited_backward.add(curr_node)
#             if curr_node in visited_forward:
#                 break
#             for neighbor in adj_list[curr_node]:
#                 if neighbor not in visited_backward:
#                     queue_backward.append(neighbor)
#                     distances_backward[neighbor] = distances_backward[curr_node] + 1
#
#     # Check if all nodes in the visitNodes array have been visited
#     for node in visitNodes:
#         if node not in distances_forward or node not in distances_backward:
#             return -1
#
#     # Calculate the minimum path length by summing up the minimum distances between adjacent nodes in the visitNodes array
#     visitNodes = [1] + sorted(visitNodes) + [n]
#     min_path_length = 0
#     for i in range(len(visitNodes) - 1):
#         u, v = visitNodes[i], visitNodes[i+1]
#         min_path_length += min(distances_forward[u] + distances_backward[v], distances_forward[v] + distances_backward[u])
#
#     return min_path_length

from collections import defaultdict, deque

def minimumTreePath(n, edges, visitNodes):
    # Build an adjacency list representation of the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Set up a table to keep track of which nodes we've visited so far
    visited = {node: False for node in range(1, n+1)}
    visited[1] = True
    visited[n] = False  # we haven't reached the end yet

    # Set up a queue to perform a breadth-first search of the tree
    q = deque()
    for node in visitNodes:
        q.append(node)

    # Perform the breadth-first search
    distance = {node: 0 for node in visitNodes}
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

    # Compute the minimum distance between the start and end nodes
    min_distance = float('inf')
    for node in visitNodes:
        if distance[node] < min_distance:
            min_distance = distance[node]

    # If we haven't visited all the nodes in visitNodes, the path is unreachable
    if not all(visited.values()):
        return -1

    # Add up the distances between the nodes in visitNodes and add the minimum distance between them
    path_length = sum(distance.values()) + (len(visitNodes) - 1) * min_distance
    return path_length


n = 5
edges = [(1, 2), (1, 3), (3, 4), (3, 5)]
visitNodes = [2, 4]

print(minimumTreePath(n, edges, visitNodes))
