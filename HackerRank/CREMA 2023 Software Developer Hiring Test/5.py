# #
# # Complete the 'minimumTreePath' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. 2D_INTEGER_ARRAY edges
# #  3. INTEGER_ARRAY visitNodes
# #

from collections import deque

def minimumTreePath(n, edges, visitNodes):
    # Create an adjacency list to represent the unweighted tree
    adj_list = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # Start a BFS from node 1 and visit all nodes in the visitNodes array
    visited = set()
    distances = {1: 0}
    queue = deque([1])
    while queue:
        curr_node = queue.popleft()
        visited.add(curr_node)
        for neighbor in adj_list[curr_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                distances[neighbor] = distances[curr_node] + 1
    for node in visitNodes:
        if node not in distances:
            return -1

    # Calculate the minimum path length by summing up the minimum distances between adjacent nodes in the visitNodes array
    visitNodes = [1] + sorted(visitNodes) + [n]
    min_path_length = 0
    for i in range(len(visitNodes) - 1):
        u, v = visitNodes[i], visitNodes[i + 1]
        min_path_length += distances[u] + distances[v] - 2 * distances[lca(adj_list, u, v)]

    return min_path_length


# Function to find the lowest common ancestor of two nodes in a tree
def lca(adj_list, u, v):
    depth = {1: 0}
    parent = {1: None}
    stack = [1]
    while stack:
        curr_node = stack.pop()
        for neighbor in adj_list[curr_node]:
            if neighbor != parent[curr_node]:
                parent[neighbor] = curr_node
                depth[neighbor] = depth[curr_node] + 1
                stack.append(neighbor)
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


n = 5
edges = [(1, 2), (1, 3), (3, 4), (3, 5)]
visitNodes = [2, 4]

print(minimumTreePath(n, edges, visitNodes))
