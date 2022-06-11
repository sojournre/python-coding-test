# 1. DFS 구현
# 2. BFS 구현
from collections import deque


def dfs(num):
    print(num, end=' ')
    visited[num] = 1

    for i in range(N + 1):
        if visited[i] == 0 and graph[num][i] == 1:
            dfs(i)


def bfs(num):
    queue = deque()
    queue.append(num)
    visited[num] = 0

    while queue:
        num = queue.popleft()
        print(num, end=' ')
        for i in range(N + 1):
            if visited[i] == 1 and graph[num][i] == 1:
                queue.append(i)
                visited[i] = 0


N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
bfs(V)
