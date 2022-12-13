import collections
from heapq import heappush, heappop


def solution(s1, s2, k):

    # 전체 그래프 생성
    graph = collections.defaultdict(list)
    for x, y in zip(s1, s2):
        graph[y].append(x)

    answer, leafs = [], []

    # k에 관련된 그래프 생성
    stack = [k]
    visited = {k}
    graph_k = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)    # 진입차수
    while stack:
        node = stack.pop()
        if graph[node]:
            for prev in graph[node]:
                indegrees[node] += 1
                graph_k[prev].append(node)
                if prev not in visited:
                    stack.append(prev)
                    visited.add(prev)
        else:
            heappush(leafs, node)

    # 위상정렬
    while leafs:
        node = heappop(leafs)
        answer.append(node)
        for next_node in graph_k[node]:
            indegrees[next_node] -= 1
            if not indegrees[next_node]:
                heappush(leafs, next_node)

    return answer


s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k = "B"
# answer = ["D", "H", "E", "C", "F", "B"]
sol = solution(s1, s2, k)
print(sol)