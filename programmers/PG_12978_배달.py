import collections
import heapq


def solution(N, road, K):
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    print(graph)

    # 큐 변수: [(시간, 정점, 남은 가능 시간)]
    Q = [(0, 1, K)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while Q:
        time, node, k = heapq.heappop(Q)
        if node not in dist:
            if k >= 0:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v, k - w))
    print(dist)
    # K 이하의 최단 경로
    return len(dist)


N = 6
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
road = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
K = 4
print(solution(N, road, K))
