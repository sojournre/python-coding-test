import collections
import heapq
from sys import stdin

input = stdin.readline
N, K = map(int, input().split())

# dx = [-1, 1]

Q = [(0, N)]
dist = collections.defaultdict(int)

while Q:
    time, node = heapq.heappop(Q)
    if node == K:
        print(time)
        break

    if node not in dist and 0 <= node <= 100000: # 두번째 조건 안주면 메모리 초과
        dist[node] = time
        time += 1
        heapq.heappush(Q, (time, node - 1))
        heapq.heappush(Q, (time, node + 1))
        heapq.heappush(Q, (time, node * 2))

