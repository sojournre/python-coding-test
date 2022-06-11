# DFS 를 통해 방문되는 노드의 전체 수를 구하는 문제
def dfs(num):
    # print(num, end=' ')
    visited[num] = 1

    for i in range(N + 1):
        if visited[i] == 0 and graph[num][i] == 1:
            dfs(i)


N = int(input())
M = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(visited.count(1) - 1)