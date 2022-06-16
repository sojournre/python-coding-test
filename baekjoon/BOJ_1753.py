import collections
import heapq
from sys import stdin

input = stdin.readline # 이거 없이 돌리면 시간 초과
graph = collections.defaultdict(list)

V, E = map(int, input().split())
K = int(input())
for i in range(E):
    u, v, w = map(int, input().split())
    # 그래프 인접 리스트 구성
    graph[u].append((v, w))

# print(graph)

# 큐 변수: [(소요 시간, 정점)]
Q = [(0, K)]
dist = collections.defaultdict(list)

# 우선 순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))

# print(dist)
# print(dist.values())
# print(dist.items())

for i in range(1, V + 1):
    if i in dist.keys():
        print(dist[i])
    else:
        print("INF")
